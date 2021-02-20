cd assets
java -jar "%~dp0/closure-compiler.jar" -O WHITESPACE_ONLY live2d.js --js_output_file live2d.min.js
java -jar "%~dp0/closure-compiler.jar" -O SIMPLE waifu-tips.js --js_output_file waifu-tips.min.js
pause