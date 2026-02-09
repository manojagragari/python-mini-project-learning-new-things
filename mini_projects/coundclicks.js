function countClicks() {
    const x=document.getElementById("btn");
    const y=document.getElementById("clickCount");
    if(x.clicked===undefined){
        x.clicked=0;
    }else{
        x.clicked+=1;
        y.innerHTML=x.clicked+" clicks";

    }
}