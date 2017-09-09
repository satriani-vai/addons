odoo.define('restrict_export.restrict_export', function (require) {
"use strict";
	var core = require('web.core');
	var Model = require('web.DataModel');
	var QWeb = core.qweb;
	var _translate = core._t;
	var Sidebar = require('web.Sidebar');

	Sidebar.include({
		add_items: function(section_code, items) {
			var self = this;
			var _super = self._super;
			var args = arguments;
			var model = this.__parentedParent.model

			var Users = new Model('res.users');
			var Values = new Model('ir.values');
			var restrict_models = [];

			Values.call('get_default', ['base.config.settings', 'restrict_models']).done( function(str_models) {
				if (str_models){restrict_models = str_models.split(",");}

				Users.call('has_group', ['restrict_export.export_data_group']).done(function(is_employee) {
					if(is_employee || restrict_models.indexOf(model) < 0){
						_super.apply(self, args);
					}
					else{
						var export_label = _translate("Export"); 
						var new_items = items;
						if (section_code == 'other') {
							new_items = [];
							for (var i = 0; i < items.length; i++) {
								if (items[i]['label'] != export_label) {
									new_items.push(items[i]);
								};
							};
						};
						if (new_items.length > 0) {
							_super.call(self, section_code, new_items);
						};
					}
				});

			})
		},
	});
}
)