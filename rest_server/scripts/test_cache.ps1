# PowerShell script to test caching on /api/items/
# Steps:
# 1. GET list (save Date header and count)
# 2. POST a new item
# 3. GET list immediately (expect same Date header if cached)
# 4. Wait 65 seconds
# 5. GET list again (expect Date changed and new item present)

$base = 'http://127.0.0.1:8000/api/items/'
Write-Host "Testing cache for $base`n"

# Helper to get Date header and parsed JSON
function Get-List {
    param($label)
    $resp = Invoke-WebRequest -Uri $base -Method Get
    $date = $resp.Headers['Date']
    $cachedAt = $null
    if ($resp.Headers['X-Cached-At']) { $cachedAt = $resp.Headers['X-Cached-At'] }
    $body = $resp.Content | ConvertFrom-Json
    $count = if ($body.results) { $body.results.Count } else { ($body | Measure-Object).Count }
    Write-Host "[$label] Date: $date  | X-Cached-At: $cachedAt | Results count: $count"
    if ($body.results) {
        Write-Host "  Results (id : name):"
        foreach ($it in $body.results) {
            Write-Host "    $($it.id) : $($it.name)"
        }
    }
    return @{ date = $date; cachedAt = $cachedAt; body = $body }
}

# 1. GET list (initial)
$first = Get-List -label 'First GET'

# 2. POST create a temporary item
$rand = Get-Random -Minimum 1000 -Maximum 9999
$new = @{ name = "TempItem-$rand"; description = 'temp for cache test'; price = '1.00' } | ConvertTo-Json
$postResp = Invoke-RestMethod -Uri $base -Method Post -Body $new -ContentType 'application/json'
Write-Host "POSTed new item: $($postResp.name) (id $($postResp.id))`n"

# 3. GET list immediately
$second = Get-List -label 'Second GET (immediate)'

if ($first.date -eq $second.date) {
    Write-Host "=> Response appears cached (Date header equal).`n" -ForegroundColor Yellow
} else {
    Write-Host "=> Response not cached (Date header different).`n" -ForegroundColor Green
}

# 4. Wait 65 seconds
Write-Host "Waiting 65 seconds for cache to expire...`n"
Start-Sleep -Seconds 65

# 5. GET list after wait
$third = Get-List -label 'Third GET (after wait)'

if ($third.date -ne $second.date) {
    Write-Host "=> Cache expired (Date header changed).
             Check that new item appears in results." -ForegroundColor Green
} else {
    Write-Host "=> Cache still present (Date header unchanged)." -ForegroundColor Yellow
}

# Try to locate the new item in the third response
$found = $false
if ($third.body.results) {
    foreach ($it in $third.body.results) {
        if ($it.name -eq $postResp.name) { $found = $true; break }
    }
}
if ($found) { Write-Host "New item found in list." -ForegroundColor Green } else { Write-Host "New item NOT found in list." -ForegroundColor Yellow }

Write-Host "\nDone."