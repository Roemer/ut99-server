cd %*
for /f "delims=" %%A in ('cd') do (
    set foldername=%%~nxA
)
tar -cvzf ..\%foldername%.tar.gz *.*
cd ..
pause