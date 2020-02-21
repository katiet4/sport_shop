a = 0;
block = document.getElementsByClassName('bottom-order');
detailBox = () => {
  if(a==0){
    block[0].style.display = 'block';
     a++;
  } else {
    block[0].style.display = 'none';
      a--;
  }
};

show = (item) => {
    info = document.getElementsByClassName('a-i-block');
    order = document.getElementsByClassName('a-o-block');
    control = document.getElementsByClassName('a-c-block');
    if(item == 'info'){
        info[0].style.display='block'
        order[0].style.display='none'
        control[0].style.display='none'
    }else if(item == 'order'){
        info[0].style.display='none'
        order[0].style.display='block'
        control[0].style.display='none'
    }else{
        info[0].style.display='none'
        order[0].style.display='none'
        control[0].style.display='block'
    }
}
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


