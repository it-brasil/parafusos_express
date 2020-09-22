odoo.define('pos_set_quantity.screens', function (require) {
    "use strict";
    
    var pos_screens = require('point_of_sale.screens');
    var gui = require('point_of_sale.gui');
    var PopupWidget = require('point_of_sale.popups');

    pos_screens.ProductScreenWidget.include({
        click_product: function(product) {
            if(product.to_weight && this.pos.config.iface_electronic_scale){
                this.gui.show_screen('scale', {product: product});
            }else{
                this.gui.show_popup('pos-set-quantity', {product: product});
            }
         },
    });

    var SetQtyPopupWidget = PopupWidget.extend({
        template: 'SetQtyPopupWidget',
        init(parent, options) {
            this._super(parent, options);
            this.options = options;
        },
        show: function (options) {
            var self = this;
            this._super(options);

            this.$(".confirm").click(function(ev) {
                var quantity = parseFloat(self.$(".input-set-qty").val().replace(",", "."));
                if(quantity > 0){
                    self.pos.get_order().add_product(self.options.product, { quantity: quantity });
                } else {
                    alert("A quantidade deve ser maior que 0!");
                    ev.stopPropagation();
                }
            });

            this.$(".input-set-qty").keypress(function(ev) {
                var keyCode = ev.keyCode || ev.which;
                if(keyCode == '13'){
                    self.$(".confirm").trigger("click");
                }
            })

            this.$(".input-set-qty").focus();
        }
    });
    gui.define_popup({name:'pos-set-quantity', widget: SetQtyPopupWidget});


});
