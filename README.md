# MIHD - Matrix Systems : Sequential Number for Barcode
[Link] https://www.odoo.com/web#id=3364903&cids=3&menu_id=4720&action=4665&active_id=3364897&model=project.task&view_type=form

## Steps to complete the dev
- [X] create a model file and inherit 'product.template' model
- [X] add a selection field and named it 'product_group' and some demo options for the field
- [X] inherit product template form view and add 'product_group' field to the view
- [X] override the '_compute_barcode' function
- [X] create a data file for the sequence rule

## Issues/Blocking points
- [X] I tried not to let the barcode to increase whenever I change product_group in the product_template
- [X] I came up with a temporary variable to store the sequence, the sequence is only generate whenever it is first chosen.
- [X] Testing

## Topics I need clarification on
- [X] Interaction between front-end part that connects to a field in backend

## Interns who helped me
[JICH] - 5 mins - Discussing task
[FEGU] - 5 mins - Remind me of data file that contains of sequence rule
## Interns who I helped
[JICH] - 5 mins - Discussing task
