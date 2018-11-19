-- Test Dataset
--HamoPK relation analysis
Select * from datamining.test where '?' in (hamopk8, hamopk9,hamopk10,hamopk11,hamopk12,hamopk13,hamopk21)
and playmethod='string';


select frameid,note, playmethod, class1, count(class1) / 2 from datamining.test
Group By class1, playmethod, note, frameid;

-- Important count statistic
select class2, count(class2) / 2 as "Count" from datamining.test
Group By class2;


select sum(sub.A) from (
	select class2, count(class2) as A from datamining.test
	Group By class2
) as sub
where sub.class2 LIKE 'aero%';

select sum(sub.B) from (
	select class2, count(class2) as B from datamining.test
	Group By class2
) as sub
where sub.class2 LIKE 'chrod%';


--Train dataset
Select mix1_instrument, COUNT(mix1_instrument) from datamining.train
Group by mix1_instrument
Union
Select mix2_instrument, COUNT(mix2_instrument) from datamining.train
Group by mix2_instrument;

Select mix1_instrument , mix2_instrument from datamining.train 
Group by mix1_instrument, mix2_instrument;