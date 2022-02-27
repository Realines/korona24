

$(document).ready(function() { 
    if (window.innerWidth < 992) { 
        var oldtop =  $(window).scrollTop();
        var scroll_button = $('.body_scroll_head')
        $( window ).scroll(function() {
            
            if (window.innerWidth < 992) { 
                var top = $(window).scrollTop();
                if(top < (oldtop + 200)){
                // console.log(`${top} ${oldtop} ${top-oldtop}`) 
                    if((top-oldtop) > 30)
                    { 
                        scroll_button.hide()
                    }
                    else if((top-oldtop) < -30)
                    {  
                        scroll_button.show()
                    }
                    oldtop = top
                } 
            }
        });
    }
    
})