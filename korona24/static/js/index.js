function mainSlider() {
    var swiper = new Swiper('.main .swiper-container', {
        // slidesPerView: 1,
        spaceBetween: 0,
        effect: "fade",
        speed: 1000,
        pagination: {
            el: '.main .swiper-pagination',
            type: 'fraction',
            clickable: true,
        },
        navigation: {
            nextEl: '.main .swiper-button-next',
            prevEl: '.main .swiper-button-prev',
        },
        breakpoints: {
            320: {
                slidesPerView: 1,
                spaceBetween: 0,

            },
            480: {
                slidesPerView: 1,
                spaceBetween: 0
            },
            1200: {
                // slidesPerView: 1,
                spaceBetween: 0
            }
        }
    });

    if (swiper.slides) {
        for (var i = 1; i < swiper.slides.length + 1; i++) {
            if (i === 1) {
                // add active class if it is the first bullet
                $('#bullets').append('<span class="swiper-pagination-bullet' + ' ' + 'swiper-pagination-bullet-active' + ' ' + 'slide' + i + '"></span>');
            } else {
                $('#bullets').append('<span class="swiper-pagination-bullet' + ' ' + 'slide' + i + '"></span>');
            }
        }
    }
    // Generate pagination bullets inside div with #bullets ID



    // ADD ACTIVE CLASS TO THE CURRENT BULLET

    // get all bullet elements
    var bullets = $('.swiper-pagination-bullet');

    swiper.on('slideChange', function() {
        // Get current slide from fraction pagination number
        var slide = "slide" + ($('.swiper-pagination-current').html());
        // Remove active class from all bullets
        bullets.removeClass("swiper-pagination-bullet-active");
        // Check each bullet element if it has slideNumber class
        $.each(bullets, function(index, value) {
            if ($(this).hasClass(slide)) {
                $(this).addClass("swiper-pagination-bullet-active");
                return false;
            }
        });
    });

}

function expertSlider() {
    var swiper = new Swiper('.expert .swiper-container', {
        slidesPerView: 3,
        spaceBetween: 30,
        loop: true,
        speed: 1000,
        pagination: {
            el: '.expert .swiper-pagination',
            type: 'fraction',
            clickable: true,
        },
        navigation: {
            nextEl: '.expert .swiper-button-next',
            prevEl: '.expert .swiper-button-prev',
        },
        breakpoints: {
            320: {
                slidesPerView: 2,
                spaceBetween: 20,

            },
            480: {
                slidesPerView: 3,
                spaceBetween: 20
            },
            992: {
                slidesPerView: 3,
                spaceBetween: 30
            }
        }
    });
}

function feedbackSlider() {
    var swiper = new Swiper('.feedback .swiper-container', {
        slidesPerView: 2,
        spaceBetween: 30,
        loop: true,
        speed: 1000,
        pagination: {
            el: '.feedback .swiper-pagination',
            type: 'fraction',
            clickable: true,
        },
        navigation: {
            nextEl: '.feedback .swiper-button-next',
            prevEl: '.feedback .swiper-button-prev',
        },
        breakpoints: {
            320: {
                slidesPerView: 1,
                spaceBetween: 20,

            },
            1200: {
                slidesPerView: 2,
                spaceBetween: 30
            }
        }
    });
}

function ourFeedbackSlider() {
    var swiper = new Swiper('.our-feedback .swiper-container', {
        slidesPerView: 1,
        spaceBetween: 30,
        effect: "fade",
        speed: 1000,
        pagination: {
            el: '.our-feedback .swiper-pagination',
            type: 'fraction',
            clickable: true,
        },
        navigation: {
            nextEl: '.our-feedback .swiper-button-next',
            prevEl: '.our-feedback .swiper-button-prev',
        },
        breakpoints: {
            320: {
                slidesPerView: 1,
                spaceBetween: 0,

            },
            480: {
                slidesPerView: 1,
                spaceBetween: 0
            },
            1200: {
                slidesPerView: 1,
                spaceBetween: 30
            }
        }
    });
}

function dmsSlider() {
    var swiper = new Swiper('.dms .swiper-container', {
        slidesPerView: 'auto',
        spaceBetween: 50,
        speed: 1000,
        pagination: {
            el: '.dms .swiper-pagination',
            type: 'fraction',
            clickable: true,
        },
        navigation: {
            nextEl: '.dms .swiper-button-next',
            prevEl: '.dms .swiper-button-prev',
        },
        breakpoints: {
            320: {
                slidesPerView: 'auto',
                spaceBetween: 20,
            },
            1200: {
                slidesPerView: 'auto',
                spaceBetween: 50,
            }
        }
    });
}

$(document).ready(function() {
    mainSlider()
    expertSlider()
    feedbackSlider()
    dmsSlider()
    ourFeedbackSlider()

    $("input").change(function() {
        let inputValue = $(this).val()
        if (inputValue) {
            $(this).addClass("input-filled")
        } else {
            $(this).removeClass("input-filled")
        }
    })

    $("input").keydown(function() {
        let inputValue = $(this).val()
        if (inputValue) {
            $(this).addClass("input-filled")
        } else {
            $(this).removeClass("input-filled")
        }

    })


    $(".header__service-btn").click(function() {
        $(this).toggleClass("header__service-btn--active")
    })

    $(".price__item-show").click(function() {
        if ($(this).hasClass("price__item-show--active")) {
            $(this).removeClass("price__item-show--active")
            $(this).siblings(".price__item-hidden").slideUp()
        } else {
            $(".price__item-show").removeClass("price__item-show--active")
            $(this).addClass("price__item-show--active")
            $(".price__item-hidden").slideUp()
            $(this).siblings(".price__item-hidden").slideDown()
        }
    })

    $(".header__burger").click(function() {
        $(this).toggleClass("header__burger--active")
        $(".header").toggleClass("header--active")
            // $(".header__right").slideToggle()
    })

})