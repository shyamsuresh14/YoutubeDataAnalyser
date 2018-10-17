function analyse(fileName){
    const exec = require("child_process").exec;
    //executes the python file and gets the output from the stdout stream and displays it
    exec('python backend/analytics/g6.py ' + fileName, function(err, stdout, stderr){
        console.log("Executing...");
        console.log(stdout + stderr);
        swal(stdout);
    });
    console.log(fileName);
}

//window.onload = support();