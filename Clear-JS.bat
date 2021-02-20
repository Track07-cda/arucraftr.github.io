cd js
java -jar "%~dp0/closure-compiler.jar" -O SIMPLE scrollreveal.js --js_output_file scrollreveal.min.js
java -jar "%~dp0/closure-compiler.jar" -O SIMPLE general.js --js_output_file general.min.js
pause