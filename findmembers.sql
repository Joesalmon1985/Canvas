DROP TABLE if exists ward01; 
DROP TABLE if exists ward02; 
DROP TABLE if exists ward03; 
DROP TABLE if exists ward04; 
DROP TABLE if exists ward05; 
DROP TABLE if exists ward06; 
DROP TABLE if exists ward07; 
DROP TABLE if exists ward08; 
DROP TABLE if exists ward09; 
DROP TABLE if exists ward10; 
DROP TABLE if exists ward11; 
DROP TABLE if exists ward12; 
DROP TABLE if exists ward13; 
DROP TABLE if exists ward14; 
DROP TABLE if exists ward15; 
DROP TABLE if exists ward16; 
DROP TABLE if exists ward17; 
DROP TABLE if exists ward18; 
DROP TABLE if exists ward19; 
DROP TABLE if exists ward20; 
DROP TABLE if exists ward21; 
DROP TABLE if exists ward22; 
DROP TABLE if exists ward23; 
DROP TABLE if exists ward24; 
DROP TABLE if exists ward25; 
DROP TABLE if exists ward26; 
DROP TABLE if exists ward27; 
DROP TABLE if exists ward28; 
DROP TABLE if exists ward29; 


.mode csv
.import P141201_Chapel_Allerton.csv ward07
.import 1502_Chapel_Allerton.csv ward01
.import 1503_Chapel_Allerton.csv ward02

drop table if exists alldata;
CREATE TABLE alldata(
  "pd" TEXT,
  "eno" TEXT,
  "stat" TEXT,
  "title" TEXT,
  "firstname" TEXT,
  "initials" TEXT,
  "surname" TEXT,
  "suffix" TEXT,
  "dateofattainment" TEXT,
  "franchiseflag" TEXT,
  "address1" TEXT,
  "address2" TEXT,
  "address3" TEXT,
  "address4" TEXT,
  "address5" TEXT,
  "address6" TEXT,
  "address7" TEXT,
  "optout" TEXT,
  "postcode" TEXT
);


insert into alldata select * from ward01;
insert into alldata select * from ward02;
insert into alldata select * from ward03;
insert into alldata select * from ward04;
insert into alldata select * from ward05;
insert into alldata select * from ward06;
insert into alldata select * from ward07;
insert into alldata select * from ward08;
insert into alldata select * from ward09;
insert into alldata select * from ward10;
insert into alldata select * from ward11;
insert into alldata select * from ward12;
insert into alldata select * from ward13;
insert into alldata select * from ward14;
insert into alldata select * from ward15;
insert into alldata select * from ward16;
insert into alldata select * from ward17;
insert into alldata select * from ward18;
insert into alldata select * from ward19;
insert into alldata select * from ward20;
insert into alldata select * from ward21;
insert into alldata select * from ward22;
insert into alldata select * from ward23;
insert into alldata select * from ward24;
insert into alldata select * from ward25;
insert into alldata select * from ward26;
insert into alldata select * from ward27;
insert into alldata select * from ward28;
insert into alldata select * from ward29;


drop table if exists fulldata;
CREATE TABLE fulldata(
  "pd" TEXT,
  "eno" TEXT,
  "stat" TEXT,
  "title" TEXT,
  "firstname" TEXT,
  "initials" TEXT,
  "surname" TEXT,
  "suffix" TEXT,
  "dateofattainment" TEXT,
  "franchiseflag" TEXT,
  "address1" TEXT,
  "address2" TEXT,
  "address3" TEXT,
  "address4" TEXT,
  "address5" TEXT,
  "address6" TEXT,
  "address7" TEXT,
  "optout" TEXT,
  "postcode" TEXT
);


insert into fulldata select * from alldata where stat is not 'D';

drop table if exists toremove;
CREATE TABLE toremove(
  "pd" TEXT,
  "eno" TEXT,
  "stat" TEXT,
  "title" TEXT,
  "firstname" TEXT,
  "initials" TEXT,
  "surname" TEXT,
  "suffix" TEXT,
  "dateofattainment" TEXT,
  "franchiseflag" TEXT,
  "address1" TEXT,
  "address2" TEXT,
  "address3" TEXT,
  "address4" TEXT,
  "address5" TEXT,
  "address6" TEXT,
  "address7" TEXT,
  "optout" TEXT,
  "postcode" TEXT
);

insert into toremove select * from alldata where stat is 'D';
alter table toremove add column toremove;
UPDATE toremove SET toremove = 'toremove';

drop table if exists removedfulldata;
CREATE TABLE removedfulldata(
  "pd" TEXT,
  "eno" TEXT,
  "stat" TEXT,
  "title" TEXT,
  "firstname" TEXT,
  "initials" TEXT,
  "surname" TEXT,
  "suffix" TEXT,
  "dateofattainment" TEXT,
  "franchiseflag" TEXT,
  "address1" TEXT,
  "address2" TEXT,
  "address3" TEXT,
  "address4" TEXT,
  "address5" TEXT,
  "address6" TEXT,
  "address7" TEXT,
  "optout" TEXT,
  "postcode" TEXT,
  "toremove" 
);

insert into removedfulldata (pd, eno, stat, title, firstname, initials, surname, suffix, dateofattainment, franchiseflag, address1, address2, address3, address4, address5, address6, address7, postcode, toremove) select fulldata.pd, fulldata.eno, fulldata.stat, fulldata.title, fulldata.firstname, fulldata.initials, fulldata.surname, fulldata.suffix, fulldata.dateofattainment, fulldata.franchiseflag, fulldata.address1, fulldata.address2, fulldata.address3, fulldata.address4, fulldata.address5, fulldata.address6, fulldata.address7, fulldata.postcode, toremove.toremove 
from fulldata left outer join toremove on fulldata.firstname = toremove.firstname and fulldata.surname = toremove.surname and fulldata.address1 = toremove.address1;

drop table if exists uptodatecouncildata;
CREATE TABLE uptodatecouncildata(
  "pd" TEXT,
  "eno" TEXT,
  "stat" TEXT,
  "title" TEXT,
  "firstname" TEXT,
  "initials" TEXT,
  "surname" TEXT,
  "suffix" TEXT,
  "dateofattainment" TEXT,
  "franchiseflag" TEXT,
  "address1" TEXT,
  "address2" TEXT,
  "address3" TEXT,
  "address4" TEXT,
  "address5" TEXT,
  "address6" TEXT,
  "address7" TEXT,
  "optout" TEXT,
  "postcode" TEXT
);

insert into uptodatecouncildata (pd, eno, stat, title, firstname, initials, surname, suffix, dateofattainment, franchiseflag, address1, address2, address3, address4, address5, address6, address7, postcode) select pd, eno, stat, title, firstname, initials, surname, suffix, dateofattainment, franchiseflag, address1, address2, address3, address4, address5, address6, address7, postcode from removedfulldata where toremove is not 'toremove';

delete from uptodatecouncildata where rowid not in 
(select min(rowid) from uptodatecouncildata group by firstname, surname, address1);

drop table if exists members;
.import members.csv members
alter table members add column partymember;
update members set partymember = 'yes'; 

update members set postcode = upper(postcode);

drop table if exists membercouncildata;
CREATE TABLE membercouncildata(
  "pd" TEXT,
  "eno" TEXT,
  "stat" TEXT,
  "title" TEXT,
  "firstname" TEXT,
  "initials" TEXT,
  "surname" TEXT,
  "suffix" TEXT,
  "dateofattainment" TEXT,
  "franchiseflag" TEXT,
  "address1" TEXT,
  "address2" TEXT,
  "address3" TEXT,
  "address4" TEXT,
  "address5" TEXT,
  "address6" TEXT,
  "address7" TEXT,
  "optout" TEXT,
  "postcode" TEXT,
  "partymember",
  "email"
);
 
insert into membercouncildata (pd, eno, stat, title, firstname, initials, surname, suffix, dateofattainment, franchiseflag, address1, address2, address3, address4, address5, address6, address7, postcode, partymember, email) select uptodatecouncildata.pd, uptodatecouncildata.eno, uptodatecouncildata.stat, uptodatecouncildata.title, uptodatecouncildata.firstname, uptodatecouncildata.initials, uptodatecouncildata.surname, uptodatecouncildata.suffix, uptodatecouncildata.dateofattainment, uptodatecouncildata.franchiseflag, uptodatecouncildata.address1, uptodatecouncildata.address2, uptodatecouncildata.address3, uptodatecouncildata.address4, uptodatecouncildata.address5, uptodatecouncildata.address6, uptodatecouncildata.address7, uptodatecouncildata.postcode, members.partymember, members.email  
from uptodatecouncildata left outer join members on uptodatecouncildata.firstname = members.firstname and uptodatecouncildata.surname = members.lastname and uptodatecouncildata.postcode = members.postcode;


.headers on
.output membercouncildata.csv
select * from membercouncildata;
.output stdout

drop table if exists onlymembercouncildata;
CREATE TABLE onlymembercouncildata(
  "pd" TEXT,
  "eno" TEXT,
  "stat" TEXT,
  "title" TEXT,
  "firstname" TEXT,
  "initials" TEXT,
  "surname" TEXT,
  "suffix" TEXT,
  "dateofattainment" TEXT,
  "franchiseflag" TEXT,
  "address1" TEXT,
  "address2" TEXT,
  "address3" TEXT,
  "address4" TEXT,
  "address5" TEXT,
  "address6" TEXT,
  "address7" TEXT,
  "optout" TEXT,
  "postcode" TEXT,
  "partymember",
  "email"
);

insert into onlymembercouncildata select * from membercouncildata where partymember is 'yes';



.headers on
.output onlymembercouncildata.csv 
select * from onlymembercouncildata;
.output stdout
