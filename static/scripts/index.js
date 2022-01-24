$(document).ready(function(){
    let position = 0;
    const sliderToShow = 6;
    const sliderToScroll = 1;
    const container = $('.slider-container');
    const track = $('.slider-track');
    const item = $('.slider-item');
    const btnPrev = $('.prev')
    const btnNext = $('.next')
    const itemsCount = item.length;
    const itemWidth = container.width() / sliderToShow;
    const movePosition = sliderToScroll * itemWidth;

    item.each(function(index, item){
        $(item).css({
            minWidth: itemWidth,
        });
    });

    btnPrev.click(function(){
        const itemsLeft = Math.abs(position) / itemWidth;
        position += itemsLeft >= sliderToScroll ? movePosition : itemsLeft * itemWidth;
        setPosition();
        chekBtns();
    });
    btnNext.click(function(){
        const itemsLeft = itemsCount - (Math.abs(position) + sliderToShow * itemWidth) / itemWidth;
        position -= itemsLeft >= sliderToScroll ? movePosition : itemsLeft * itemWidth;
        setPosition();
        chekBtns();
    });

    const setPosition = () => {
        track.css({
            transform: `translateX(${position}px)`
        });
    };

    const chekBtns = () => {
        btnNext.prop(
            'disabled',
            position <= -(itemsCount - sliderToShow) * itemWidth
        );
        btnPrev.prop('disabled', position === 0);
    };

    chekBtns();
});