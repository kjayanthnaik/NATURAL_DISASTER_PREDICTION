var img= ["http://blog.newhomesource.com/wp-content/uploads/2019/12/lightning.jpg",
  "https://clovered.com/wp-content/uploads/2020/05/10-Top-Emergency-Preparedness-Tips-for-Natural-Disasters-1000px-min.jpg", 
  "https://www.pandotrip.com/wp-content/uploads/2014/01/kansas-Phil-Degginger.jpg", 
 
   "https://fact24.com/wp-content/uploads/2020/08/fact24-applications-naturaldisaster-floodingH500px_Q60.jpg",
   "https://www.holidify.com/images/cmsuploads/compressed/officiallynologo1174400271710104179145826729903381098730917n_20200814191132.jpg",
   "https://riskandinsurance.com/wp-content/uploads/2021/02/natural-disaster.jpg",
   "https://nypost.com/wp-content/uploads/sites/2/2018/01/20180122_zaa_p133_322.jpg?quality=80&strip=all",
   "https://i.ytimg.com/vi/a3d7tJhMc1k/maxresdefault.jpg"
];

var i=0;

function im(){
    
    if(i<img.length){
        
      let sr=document.getElementById('img');
      sr.src=img[i];
      
      i++;
    }
    else{
        
        i=0;
    }
    
}

setInterval(im,100);