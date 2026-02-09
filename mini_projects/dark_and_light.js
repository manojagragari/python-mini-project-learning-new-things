function fun(){
    const b=document.getElementById("btn");
    if(document.body.style.backgroundColor==="white"){
        document.body.style.backgroundColor="black";
        document.body.style.color="white";
        b.innerHTML="Light Mode";
    }else{
        document.body.style.backgroundColor="white";
        document.body.style.color="black";
        b.innerHTML="Dark Mode";
    }
}