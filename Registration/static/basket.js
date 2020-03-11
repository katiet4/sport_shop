b = document.getElementsByClassName('i-p');

var prices = []; // для цен

for(var i = 0; i < b.length;i++){
	prices.push(b[i].innerText);
	console.log(prices);
}
summ();


//суммирует все и добавляет изменения в итог
function summ() {
	var result = 0;
	for(var i = 0; i < b.length;i++){
		result += parseInt(b[i].innerText);
	}
	document.getElementById("hiddenResult").value = result;
	document.getElementById("result").innerHTML = "Итого: " + result + "₽";
}

plus = (i) => {
	c = ++(document.getElementById(i).value);
	b[i].innerHTML = parseInt(prices[i]) * c;
	summ();
}

minus = (i) => {
    if(elem = document.getElementById(i).value != 1){
        c = --(document.getElementById(i).value);
		b[i].innerHTML = parseInt(prices[i]) * c;
		summ();
    }
}
