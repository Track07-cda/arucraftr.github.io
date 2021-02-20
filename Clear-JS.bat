cd js
java -jar "%~dp0/closure-compiler.jar" -O SIMPLE scrollreveal.js general.js --js_output_file models.min.js
pause