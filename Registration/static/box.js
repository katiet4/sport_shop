block = document.getElementsByClassName('bottom-order');
function detailBox(numberOrder) {
  order = document.getElementById("order-"+numberOrder);
  // alert(1);
  if(order.style.display=="block"){
    order.style.display = 'none';
  } else {
    order.style.display = 'block';
  }
};
showItem = (item) =>{
    inf = document.getElementsByClassName('inf');
    ord = document.getElementsByClassName('ord'); 
    admin = document.getElementsByClassName('admin');
    if(item == 'inf'){
        inf[0].style.display='block'
        ord[0].style.display='none'
        admin[0].style.display='none'
    }else if(item == 'ord'){
        inf[0].style.display='none'
        ord[0].style.display='block'
        admin[0].style.display='none'
    }else{
        inf[0].style.display='none'
        ord[0].style.display='none'
        admin[0].style.display='block'
    }
}


