function doSomething(){
    let a = documnet.getElementById('inputA').value;
    let b = document.getElementById('inputB').value;
    document.getElementById("valueA").innerHTML = a;
    document.getElementById("valueB").innerHTML = b;
    document.getElementById("valueC").innerHTML = Number(a) + Number(b);
}