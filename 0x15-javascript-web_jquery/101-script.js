$.ready (function () {
    const target = $('ul.my_list');
    const add = $('div#add_item');
    const remove = $('div#remove_item');
    const clear = $('div#clear_list');

    add.click(() => {
        target.append('<li>Item</li>');
    });

    remove.click(() => {
        target.children().last().remove();
    });

    clear.click(() => {
        target.html('');
    });
};
