const isMobile={Android:function(){return navigator.userAgent.match(/Android/i);},BlackBerry:function(){return navigator.userAgent.match(/BlackBerry/i);},IOS:function(){return navigator.userAgent.match(/iPhone|iPad|iPod/i);},Opera:function(){return navigator.userAgent.match(/Opera Mini/i);},Windows:function(){return navigator.userAgent.match(/IEMibile/i);},any:function(){return(isMobile.Android()||isMobile.BlackBerry()||isMobile.IOS()||isMobile.Opera()||isMobile.Windows());}};function showContent(){var temp=document.getElementsByTagName("template")[0];var clon=temp.content.cloneNode(true);document.body.appendChild(clon);}
if(isMobile.any()){document.body.classList.add('_touch');showContent()}else{document.body.classList.add('_pc');};$(document).ready(function(){$('.slider').slick({dots:true,infinite:true,speed:100,slidesToShow:1,cssEase:'ease',adaptiveHeight:false,draggable:false,touchMove:false,waitForAnimate:false,variableWidth:false,touchThreshold:7,});})
jQuery(window).on('load',function(){var sizer='.sizer4';var gutter='.gutter';var container=$('#gallery');container.imagesLoaded(function(){container.masonry({itemSelector:'.item-masonry',percentPosition:true,transitionDuration:'0',});var infinite=new Waypoint.Infinite({element:$('.infinite-container')[0],container:'auto',items:'.infinite-item',more:'.infinite-more-link',offset:'bottom-in-view',loadingClass:'infinite-loading',onBeforePageLoad:function(){},onAfterPageLoad:function(){container.masonry('reloadItems');container.imagesLoaded().progress(function(){container.masonry('layout');});},});});});if(document.body.classList.contains('_touch')){rlMenu('.header__movbile-navigation','#nav-menu-mobile','.close-ham-menu')
rlMenu('.header__profile','#profile-menu-mobile','.close-ham-menu-2')
rlMenu('.btnFilter','.paper_mobile','.search-filter__head-2')}else{$('.header__profile').on('click',function(){$(this).toggleClass('_active');});$(document).on('mouseup',function(e){let s=$('.header__profile._active');if(!s.is(e.target)&&s.has(e.target).length===0){s.removeClass('_active');}});}
function rlMenu(btn,rlmenu,close){const button=document.querySelector(btn)
const menu=document.querySelector(rlmenu)
const closeHamMenu=document.querySelector(close)
button.addEventListener("click",function(e){menu.classList.toggle('_active');document.body.classList.toggle('_lock')});$(document).on('mouseup',function(e){let s=$(menu)
if(menu.classList.contains('_active')===true){if(!s.is(e.target)&&s.has(e.target).length===0){s.removeClass('_active');document.body.classList.remove('_lock')}else{if(closeHamMenu){closeHamMenu.addEventListener("click",function(e){menu.classList.remove('_active');document.body.classList.remove('_lock')});}}}});}
function btn(name,clsname){$(document).ready(function(){$(name).click(function(){$(clsname).addClass('_active');});});$(document).ready(function(){$('.search-filter__head').click(function(){$(clsname).removeClass('_active');});});}
btn('.search-filter-submenu','.search-filter-layout')
btn('.search-filter-submenu-2','.search-filter-layout-2')
let boxes=document.querySelectorAll('.checkbox');if(boxes){for(let index=0;index<boxes.length;index++){const box=boxes[index];box.addEventListener("click",function(e){box.classList.toggle('_active');});}};