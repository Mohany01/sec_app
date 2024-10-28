{
    'name' : 'Sec App' ,
    'version' :'12.0.1.0.0',
    'category':'Extra Tools',
    'summary':'second module',
    'author':'Mohammed Hany',
    'depends':['base','sale_management','mail',],
    'data':[
        'views/root_menu.xml',
        'views/property_view.xml',
        'security/ir.model.access.csv',
        'views/owner_view.xml',
        'views/tag_view.xml',
        'views/sale_order_view.xml',

    ],

    'installable':True,
    'application':True,

}