'use strict';

(function ($) {

    /*------------------
        Preloader
    --------------------*/
    $(window).on('load', function () {
        $(".loader").fadeOut();
        $("#preloder").delay(200).fadeOut("slow");

        /*------------------
            Product filter
        --------------------*/
        $('.filter__controls li').on('click', function () {
            $('.filter__controls li').removeClass('active');
            $(this).addClass('active');
        });
        if ($('.property__gallery').length > 0) {
            var containerEl = document.querySelector('.property__gallery');
            var mixer = mixitup(containerEl);
        }
    });

    /*------------------
        Background Set
    --------------------*/
    $('.set-bg').each(function () {
        var bg = $(this).data('setbg');
        $(this).css('background-image', 'url(' + bg + ')');
    });

    //Search Switch
    $('.search-switch').on('click', function () {
        $('.search-model').fadeIn(400);
    });

    $('.search-close-switch').on('click', function () {
        $('.search-model').fadeOut(400, function () {
            $('#search-input').val('');
        });
    });

    //Canvas Menu
    $(".canvas__open").on('click', function () {
        $(".offcanvas-menu-wrapper").addClass("active");
        $(".offcanvas-menu-overlay").addClass("active");
    });

    $(".offcanvas-menu-overlay, .offcanvas__close").on('click', function () {
        $(".offcanvas-menu-wrapper").removeClass("active");
        $(".offcanvas-menu-overlay").removeClass("active");
    });

    /*------------------
		Navigation
	--------------------*/
    $(".header__menu").slicknav({
        prependTo: '#mobile-menu-wrap',
        allowParentLinks: true
    });

    /*------------------
        Accordin Active
    --------------------*/
    $('.collapse').on('shown.bs.collapse', function () {
        $(this).prev().addClass('active');
    });

    $('.collapse').on('hidden.bs.collapse', function () {
        $(this).prev().removeClass('active');
    });

    /*--------------------------
        Banner Slider
    ----------------------------*/
    $(".banner__slider").owlCarousel({
        loop: true,
        margin: 0,
        items: 1,
        dots: true,
        smartSpeed: 1200,
        autoHeight: false,
        autoplay: true,
        autoplayTimeout: 5000, // Increase this value to slow down the carousel
    });

    /*--------------------------
        Product Details Slider
    ----------------------------*/
    $(".product__details__pic__slider").owlCarousel({
        loop: true,
        margin: 0,
        items: 1,
        dots: false,
        nav: true,
        navText: ["<i class='arrow_carrot-left'></i>","<i class='arrow_carrot-right'></i>"],
        smartSpeed: 1200,
        autoHeight: false,
        autoplay: false,
        mouseDrag: false,
    }).on('changed.owl.carousel', function(event) {
        var indexNum = event.item.index + 1;
        product_thumbs(indexNum);
    });

    function product_thumbs (num) {
        var thumbs = document.querySelectorAll('.product__thumb a');
        thumbs.forEach(function (e) {
            e.classList.remove("active");
            if(e.hash.split("-")[1] == num) {
                e.classList.add("active");
            }
        })
    }

    /*--------------------------
        banner Slider
    ----------------------------*/
    $(".banner__pic__slider").owlCarousel({
        loop: true,
        margin: 0,
        items: 1,
        dots: false,
        nav: true,
        navText: ["<i class='arrow_carrot-left'></i>","<i class='arrow_carrot-right'></i>"],
        smartSpeed: 2000,
        autoHeight: false,
        autoplay: true, // Enable automatic transitions
        mouseDrag: false,
        autoplayTimeout: 5000, // Set the delay between automatic transitions to 5 seconds
    }).on('changed.owl.carousel', function(event) {
        var indexNum = event.item.index + 1;
        product_thumbs(indexNum);
    });

    function product_thumbs (num) {
        var thumbs = document.querySelectorAll('.product__thumb a');
        thumbs.forEach(function (e) {
            e.classList.remove("active");
            if(e.hash.split("-")[1] == num) {
                e.classList.add("active");
            }
        })
    }
    $(".product__type__pic__slider").owlCarousel({
        loop: true,
        margin: 0,
        slideBy: 1,
        dots: false,
        nav: true,
        navText: ["<i class='arrow_carrot-left'></i>","<i class='arrow_carrot-right'></i>"],
        smartSpeed: 1200,
        autoHeight: false,
        autoplay: false,
        mouseDrag: false,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 2 
            },
            1000: {
                items: 4 
            }
        }
    }).on('changed.owl.carousel', function(event) {
        var indexNum = event.item.index + 1;
        product_thumbs(indexNum);
    });

    function product_thumbs (num) {
        var thumbs = document.querySelectorAll('.product__thumb a');
        thumbs.forEach(function (e) {
            e.classList.remove("active");
            if(e.hash.split("-")[1] == num) {
                e.classList.add("active");
            }
        })
    }

    /*------------------
		Magnific
    --------------------*/
    $('.image-popup').magnificPopup({
        type: 'image'
    });


    $(".nice-scroll").niceScroll({
        cursorborder:"",
        cursorcolor:"#dddddd",
        boxzoom:false,
        cursorwidth: 5,
        background: 'rgba(0, 0, 0, 0.2)',
        cursorborderradius:50,
        horizrailenabled: false
    });

    /*------------------
        load more option 
    --------------------*/

// Initialize MixItUp outside of the click event handler

// Initialize MixItUp outside of the click event handler

// $('#load-more').click(function() {
//     var _countproduct = $(".product-box").length;
//     var _limit = $(this).data('limit');
    
//     $.ajax({
//         url: {{ url "load_more_data-page" }},
//         data: { limit: _limit, offset: _countproduct },
//         success: function(data) {
//             $('#load-more').data('page', _countproduct / _limit + 1);
//             $('.property__gallery').append(data.html);
            
//             if (_countproduct + _limit >= data.total) {
//                 $('#load-more').hide();
//             }
//         },
//         // error: function(jqXHR, textStatus, errorThrown) {
//         //     console.error('AJAX error: ' + textStatus + ', ' + errorThrown);
//         // }
//     });
// });

/*------------------
    CountDown
--------------------*/
// For demo preview start
var today = new Date();
    var dd = String(today.getDate()).padStart(2, '0');
    var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
    var yyyy = today.getFullYear();

    if(mm == 12) {
        mm = '01';
        yyyy = yyyy + 1;
    } else {
        mm = parseInt(mm) + 1;
        mm = String(mm).padStart(2, '0');
    }
    var timerdate = mm + '/' + dd + '/' + yyyy;
    // For demo preview end


    // Uncomment below and use your date //

    /* var timerdate = "2020/12/30" */

	$("#countdown-time").countdown(timerdate, function(event) {
        $(this).html(event.strftime("<div class='countdown__item'><span>%D</span> <p>Day</p> </div>" + "<div class='countdown__item'><span>%H</span> <p>Hour</p> </div>" + "<div class='countdown__item'><span>%M</span> <p>Min</p> </div>" + "<div class='countdown__item'><span>%S</span> <p>Sec</p> </div>"));
    });

    /*-------------------
		Range Slider
	--------------------- */
	var rangeSlider = $(".price-range"),
    minamount = $("#minamount"),
    maxamount = $("#maxamount"),
    minPrice = rangeSlider.data('min'),
    maxPrice = rangeSlider.data('max');
    rangeSlider.slider({
    range: true,
    min: minPrice,
    max: maxPrice,
    values: [minPrice, maxPrice],
    slide: function (event, ui) {
        minamount.val('$' + ui.values[0]);
        maxamount.val('$' + ui.values[1]);
        }
    });
    minamount.val('$' + rangeSlider.slider("values", 0));
    maxamount.val('$' + rangeSlider.slider("values", 1));

    /*------------------
		Single Product
	--------------------*/
	$('.product__thumb .pt').on('click', function(){
		var imgurl = $(this).data('imgbigurl');
		var bigImg = $('.product__big__img').attr('src');
		if(imgurl != bigImg) {
			$('.product__big__img').attr({src: imgurl});
		}
    });
    
    /*-------------------
		Quantity change
	--------------------- */

    /*-------------------
		Radio Btn
	// --------------------- */
    $(".size__btn label").on('click', function () {
        $(".size__btn label").removeClass('active');
        $(this).addClass('active');
    });

$(document).ready(function() {
    // Hide all sections except the first one
    $('.profile-info:not(:first)').hide();

    // Show the selected section and hide all others when a link is clicked
    $('.list-group-item').click(function(e) {
        e.preventDefault();
        var target = $(this).attr('href');
        $('.profile-info').hide();
        $(target).show();
    });
});

$('.qtybtn').on('click', function(e) {
    e.preventDefault();

    var $button = $(this);
    var oldValue = $button.parent().find('input').val();
    var newVal;
    var url = $button.attr('href');
    var price = parseFloat($button.parent().parent().prev().text().substring(1));

    if ($button.hasClass('inc')) {
        newVal = parseFloat(oldValue) + 1;
    } else {
        if (oldValue > 1) {
            newVal = parseFloat(oldValue) - 1;
        } else {
            newVal = 0;
        }
    }

    var newTotal = price * newVal;

    $.ajax({
        url: url,
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            var cartTotal = parseFloat($('.cart__total__procced ul li span').last().text().substring(2)) + (newTotal - price * oldValue);

            if (newVal == 0) {
                $button.closest('tr').remove();
            } else {
                $button.parent().find('input').val(newVal);
                $button.parent().parent().next().text('$ ' + newTotal.toFixed(2));
            }

            $('.cart__total__procced ul li span').text('$ ' + cartTotal.toFixed(2));
        }
    });
});

$(document).ready(function() {
    $('.add-to-cart').click(function(e) {
        e.preventDefault();
        var url = $(this).attr('href');
        $.ajax({
            url: url,
            method: 'get',
            success: function(response) {
                $('#cart-count').text(response.cart_count);
                // Handle any other response data here
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});

$(document).ready(function() {
        $('.add-to-wishlist').click(function(e) {
            e.preventDefault();
            var url = $(this).attr('href');
            $.ajax({
                url: url,
                method: 'get',
                success: function(response) {
                    $('#wishlist-count').text(response.wishlist_count);
                    // Handle any other response data here
                },
                error: function(error) {
                    console.log(error);
                }
            });
        });
    });

$(document).ready(function() {
    $('.icon_close').click(function(e) {
        e.preventDefault();
        var url = $(this).data('url');
        var pro_id = $(this).data('pro-id');  // Define pro_id here
        $.ajax({
            url: url,
            method: 'get',
            success: function(response) {
                $('#cart-count').text(response.cart_count);
                $('#product-row-' + pro_id).remove();
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});

$(document).ready(function() {
    $('a[data-pro-id]').click(function(e) {
        e.preventDefault();
        var url = $(this).data('url');
        var pro_id = $(this).data('pro-id');
        $.ajax({
            url: url,
            method: 'get',
            success: function(response) {
                $('#wishlist-count').text(response.wishlist_count);
                $('#product-' + pro_id).remove();  // Remove the product div
            },
            error: function(error) {
                console.log(error);
            }
        });
        return false;  // Prevent the page from being refreshed
    });
});

})(jQuery);

function loadFile(event) {
    var reader = new FileReader();
    reader.onload = function(){
        var output = document.getElementById('profile-photo-img');
        output.src = reader.result;
    };
    reader.readAsDataURL(event.target.files[0]);
};

