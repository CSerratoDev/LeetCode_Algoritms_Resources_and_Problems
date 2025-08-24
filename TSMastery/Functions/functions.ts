export { };
//function name(params: dataType) : never {} 
function throwError(message: string): never {
    throw new Error(message);
}
throwError("Error :(");
// function name(params: dataType) : void {} */
function logMessage(message: string): void {
    console.log(`Log message ${message}`)
}
logMessage("This is log message");