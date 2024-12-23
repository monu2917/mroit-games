let search =document.querySelector(".search")
search.onclick=function (){
    document.querySelector(".container").classList.toggle('active');
}
let clear =document.querySelector(".clear")
clear.onclick=function (){
    let btn = document.getElementById("search")
    // btn.value="";
    if(btn.value.trim().length>0){
        btn.value=""
    }else{
        console.log(true);
        
        search.classList.toggle("hide")
    }
   
}
// clear.onclick=function (){
//     document.querySelector("search").classList.toggle('hide');
// }