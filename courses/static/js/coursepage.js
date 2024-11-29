 
    // window.onload =() =>{
       // player= document.getElementById('player')
       // maintainRatio()
   //     
   // }
   var player
   var videolist
   document.onreadystatechange=function(){
       console.log(document.readyState)
       if(document.readyState == 'interactive'){
           player = document.getElementById("player")
           videolist=document.getElementById('video_list')
           
           maintainRatio()
       }
   }
   function maintainRatio(){
       console.log({
           width: player.width,
           cw:player.clientWidth,
           h: player.height,
           ch: player.clientHeight
       })
       var w= player.clientWidth
       var h= (w*9)/16
       // console.log({w, h})
       player.height = h
       videolist.style.maxHeight=h +'px'


   }

   window.onresize= maintainRatio