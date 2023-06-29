Link to the task: https://www.odoo.com/web#id=3364899&cids=3&menu_id=4720&action=4665&active_id=3364897&model=project.task&view_type=form

QUAD: MIHD

Approaches to the problem:

Write an addon module to add new fields and overwrite the price field to calculated field
    1.First is to inherit the 'product.template' model and add as well as overwrite based on that
    2.Then I need to write a new view, also inherit from the product template view to add new fields to the UI

1- The original sales price field in the product.template model has the name "list_price"- I over wrote it 
    