$files = Get-ChildItem "%Directory Path%"

foreach ($f in $files) {
	h4toh5convert.exe $f.FullName ("%Directory Path" + $f.BaseName + ".h5")
	echo ("Working on " + $f.Fullname)
}