function changeImage() {
    var image = document.getElementById('myImage');
    if(image.src.match("download.png")){
        image.src="download4.jpg";
    }else{
        image.src="download.png";
    }
}