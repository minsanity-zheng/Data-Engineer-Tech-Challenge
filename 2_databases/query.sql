--1.list of our customers and their spending
with customer_spent as (
	Select customer_id,sum(price) as total_spent 
	from Transaction 
	group by customer_id
)
select Customer.name, customer_spent.total_spent 
from customer_spent
left join Customer
on customer_spent.customer_id = Customer.customer_id

--2.top 3 car manufacturers that customers bought by sales (quantity) and the sales number for it in the current month
--assuming the database system timezone is same as car dealer local
with model_sales_count as (
	select Model_id,count(1) as Sales_count, sum(Price) as Sales_number 
	from Transaction 
	where transation_datetime >= date_trunc('month', now()) 
	group by Model_id
)
, manufacturer_sales as (
select Manufacturer,sum(sales_count) as sales_quantity, sum(Sales_number) as Sales_number 
from model_sales_count 
left join Car 
on model_sales_count.Model_id = Car.Model_id
group by Manufacturer
)
select * from manufacturer_sales order by sales_quantity desc limit 3