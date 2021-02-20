cd assets
java -jar "%~dp0/closure-compiler.jar" -O WHITESPACE_ONLY waifu-tips.js live2d.js --js_output_file models.min.js
pause