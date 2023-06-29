# MIHD - NY P&W Shoes : Auto-calculated price
[Link] https://www.odoo.com/web#id=3364899&cids=3&menu_id=4720&action=4665&active_id=3364897&model=project.task&view_type=form

## Steps to complete the dev
- [X] Create init and manifest file for the basic structure of the module
- [X] Read the requirements of the task
- [X] Create models folder contains product_template.py file
- [X] Inherit the 'product.template' model
- [X] Create 2 new fields named 'pair_per_case' and 'price_per_pair'
- [X] Override list_price field with compute field
- [X] Write the compute function for 'list_price' based on 'pair_per_case' and 'price_per_pair'
- [X] Add detailed type for the product type as well as mapping function
- [X] Create the view and inherit the product template form view
- [X] Add 2 new fields to the view and override list_price field in the view with the read_only condition
- [X] Testing the function on odoo local machine

## Issues/Blocking points
- [X] Inherited views, xpath expr, it took me a while to find the path to inherit in the views
- [X] With the read_only for the list_price in the view, I faced a problem with the attrs in finding condition when 2 new fields are input correctly
- [X] My condition in the first try: 'readonly':['|',('pair_per_case','=', True),('price_per_pair', '=', True)] but it was incorrect
- [X] After several try, I got it worked by modified to this 'readonly':['|',('pair_per_case','!=', False),('price_per_pair', '!=', False)]

## Topics I need clarification on
- [X] Views attribute syntax

## Interns who helped me

## Interns who I helped
