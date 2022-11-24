function AddToCart(product_id){
    let count = document.getElementById('quantity').value;
    console.log(count)
    let d = {
        product_id:product_id,
        count:count,
    }
    let data = JSON.stringify(d)

	  if (window.XMLHttpRequest) {
      var xhttp=new XMLHttpRequest();
    } else {  // code for IE6, IE5
        var xhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    xhttp.onreadystatechange = function() {
    if (xhttp.readyState === 4 && xhttp.status === 200) {
      var data = JSON.parse(this.responseText);
      if (data['status'] === 200){
          var block = document.getElementById('info');
          block.classList = ['message info-show']
      }
    }else{
      console.log('not yet')

      }
    }

    var url = "/cart/add/"
    xhttp.open("GET", url+`?data=${data}`, true);
    xhttp.send();
}


let results = document.getElementById('results')
let searchBlock = document.querySelector('.liveSearch')
searchBlock.style.display = 'none'
function liveSearch (value){
    if(value === ''){
        searchBlock.style.display = 'none'
    }else{
        searchBlock.style.display = 'block'
    }
    if (window.XMLHttpRequest) {
        var xhttp=new XMLHttpRequest();
    } else {  // code for IE6, IE5
        var xhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    xhttp.onreadystatechange = function() {
        if (xhttp.readyState === 4 && xhttp.status === 200) {
            var data = JSON.parse(this.responseText);
            let products = data['products']
            let div = '<div>'
            for(item in products){
                template = ` <a href="/detail/${products[item].id}" class="nav-link text-dark">
                      <div class="media">
                     
                        <img id="product_image"
                             class="d-flex mr-3"
                             style="width: 50px; height: 50px;"
                             src="/media/${products[item].image}"
                             data-holder-rendered="true">
                        <div class="media-body">
                          <span class="mt-0" id="product_name">${products[item].name}</span>                         
                          <strong><span id="product_price">$ ${products[item].price}</span></strong>
                           <hr>
                        </div>
                      </div>
                      </a>
                `
                div += template
            }
            div += '</div>'
            results.innerHTML = div
        }else{
            console.log('Yemadi')
        }
    }
    var url = "/search/"
    xhttp.open("GET", url+`?data=${value}`, true);
    xhttp.send();
}