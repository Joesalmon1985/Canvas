-- This file contains SQL statements to create the TABLEs used to hold electoral
-- roll data. 
--
-- It is intended to be read by sqlite3
-- 
-- Before running this program, rename the most recent complete .csv copy of the register to a councilfull.csv
-- rename any monthly updates to files called council01-12.csv corresponding to the month they were sent.
-- 
-- The headings in these tables should all be in lowercase with no spaces, as in the csv file called exampleheadings.csv
--
-- If you already have a spreadsheet of canvassing data rename this to old.csv. The data within this spreadsheet must have address data in the
-- same format as the electoral register, and information such as intention and likely hood to vote green as in the file exampledata.csv
-- 
-- Finally if you have access to the members database please create a report and rename it members.csv, making sure there are no spaces in the 
-- headings of the columns for FirstName, LastName and PostCode.
--
-- Once you run createall.sql this will create a number of new  .csv files using combinations of this data.
--
-- $ sqlite3 draftfreshdata.sqlite
-- SQLite version 3.7.17 2013-05-20 00:56:22
-- Enter ".help" for instructions
-- Enter SQL statements terminated with a ";"
-- 
-- 
--
DROP TABLE councilfull; 
DROP TABLE council01;
DROP TABLE council02; 
DROP TABLE council03; 
DROP TABLE council04; 
DROP TABLE council05; 
DROP TABLE council06; 
DROP TABLE council07; 
DROP TABLE council08; 
DROP TABLE council09; 
DROP TABLE council10;
DROP TABLE council11;
DROP TABLE council12;
DROP TABLE old;
drop table members;

.mode csv
.import councilfull.csv councilfull
.import council01.csv council01
.import council02.csv council02
.import council03.csv council03
.import council04.csv council04
.import council05.csv council05
.import council06.csv council06
.import council07.csv council07
.import council08.csv council08
.import council09.csv council09
.import council10.csv council10
.import council11.csv council11
.import council12.csv council12
.import old.csv old
.import members.csv members

drop table councilfullupdated;

-- These below lines create a new table with the most up to date data from the electoral register.

CREATE TABLE councilfullupdated(
  "pd" TEXT,
  "eno" TEXT,
  "firstname" TEXT,
  "surname" TEXT,
  "fulladdress" TEXT,
  "street" TEXT,
  "address_1" TEXT,
  "address_2" TEXT,
  "address_3" TEXT,
  "address_4" TEXT,
  "address_5" TEXT,
  "address_6" TEXT,
  "address_7" TEXT,
  "v12" TEXT,
  "v14" TEXT,
  "green" TEXT,
  "intent" TEXT,
  "surveyn" TEXT,
  "knocked" TEXT
  "other1" TEXT,
  "other2" TEXT,
  "remove"
);

insert into councilfullupdated (pd,eno,firstname,surname,fulladdress,address_1,address_2,address_3,address_4,address_5,address_6,address_7, remove) select pd,eno,firstname,surname,address1||address2||address3||address4||address5||address6||address7,address1,address2,address3,address4,address5,address6,address7, remove from council01 where remove is not 'D';

insert into councilfullupdated (pd,eno,firstname,surname,fulladdress,address_1,address_2,address_3,address_4,address_5,address_6,address_7, remove) select pd,eno,firstname,surname,address1||address2||address3||address4||address5||address6||address7,address1,address2,address3,address4,address5,address6,address7, remove from council02 where remove is not 'D';

insert into councilfullupdated (pd,eno,firstname,surname,fulladdress,address_1,address_2,address_3,address_4,address_5,address_6,address_7, remove) select pd,eno,firstname,surname,address1||address2||address3||address4||address5||address6||address7,address1,address2,address3,address4,address5,address6,address7, remove from council03 where remove is not 'D';

insert into councilfullupdated (pd,eno,firstname,surname,fulladdress,address_1,address_2,address_3,address_4,address_5,address_6,address_7, remove) select pd,eno,firstname,surname,address1||address2||address3||address4||address5||address6||address7,address1,address2,address3,address4,address5,address6,address7, remove from council04 where remove is not 'D';

insert into councilfullupdated (pd,eno,firstname,surname,fulladdress,address_1,address_2,address_3,address_4,address_5,address_6,address_7, remove) select pd,eno,firstname,surname,address1||address2||address3||address4||address5||address6||address7,address1,address2,address3,address4,address5,address6,address7, remove from council05 where remove is not 'D';

insert into councilfullupdated (pd,eno,firstname,surname,fulladdress,address_1,address_2,address_3,address_4,address_5,address_6,address_7, remove) select pd,eno,firstname,surname,address1||address2||address3||address4||address5||address6||address7,address1,address2,address3,address4,address5,address6,address7, remove from council06 where remove is not 'D';

insert into councilfullupdated (pd,eno,firstname,surname,fulladdress,address_1,address_2,address_3,address_4,address_5,address_6,address_7, remove) select pd,eno,firstname,surname,address1||address2||address3||address4||address5||address6||address7,address1,address2,address3,address4,address5,address6,address7, remove from council07 where remove is not 'D';

insert into councilfullupdated (pd,eno,firstname,surname,fulladdress,address_1,address_2,address_3,address_4,address_5,address_6,address_7, remove) select pd,eno,firstname,surname,address1||address2||address3||address4||address5||address6||address7,address1,address2,address3,address4,address5,address6,address7, remove from council08 where remove is not 'D';

insert into councilfullupdated (pd,eno,firstname,surname,fulladdress,address_1,address_2,address_3,address_4,address_5,address_6,address_7, remove) select pd,eno,firstname,surname,address1||address2||address3||address4||address5||address6||address7,address1,address2,address3,address4,address5,address6,address7, remove from council09 where remove is not 'D';

insert into councilfullupdated (pd,eno,firstname,surname,fulladdress,address_1,address_2,address_3,address_4,address_5,address_6,address_7, remove) select pd,eno,firstname,surname,address1||address2||address3||address4||address5||address6||address7,address1,address2,address3,address4,address5,address6,address7, remove from council10 where remove is not 'D';

insert into councilfullupdated (pd,eno,firstname,surname,fulladdress,address_1,address_2,address_3,address_4,address_5,address_6,address_7, remove) select pd,eno,firstname,surname,address1||address2||address3||address4||address5||address6||address7,address1,address2,address3,address4,address5,address6,address7, remove from council11 where remove is not 'D';

insert into councilfullupdated (pd,eno,firstname,surname,fulladdress,address_1,address_2,address_3,address_4,address_5,address_6,address_7, remove) select pd,eno,firstname,surname,address1||address2||address3||address4||address5||address6||address7,address1,address2,address3,address4,address5,address6,address7, remove from council12  where remove is not 'D';

insert into councilfullupdated (pd,eno,firstname,surname,fulladdress,address_1,address_2,address_3,address_4,address_5,address_6,address_7, remove) select pd,eno,firstname,surname,address1||address2||address3||address4||address5||address6||address7,address1,address2,address3,address4,address5,address6,address7, remove from councilfull where remove is not 'D';

-- These lines create a new field called street.

  update councilfullupdated set street = 'ash gardens' where fulladdress glob '*ASH GARDENS*'; 
  update councilfullupdated set street = 'ash road' where fulladdress glob '*ASH ROAD*'; 
  update councilfullupdated set street = 'ash terrace' where fulladdress glob '*ASH TERRACE*'; 
  update councilfullupdated set street = 'cantebury drive' where fulladdress glob '*CANTEBURY DRIVE*'; 
  update councilfullupdated set street = 'chapel terrace' where fulladdress glob '*CHAPEL TERRACE*'; 
  update councilfullupdated set street = 'cross chapel street' where fulladdress glob '*CROSS CHAPEL STREET*';
  update councilfullupdated set street = 'dennistead crescent' where fulladdress glob '*DENNISTEAD CRESCENT*'; 
  update councilfullupdated set street = 'derwentwater grove' where fulladdress glob '*DERWENTWATER GROVE*';  
  update councilfullupdated set street = 'derwentwater terrace' where fulladdress glob '*DERWENTWATER TERRACE*'; 
  update councilfullupdated set street = 'estcourt avenue' where fulladdress glob '*ESTCOURT AVENUE*'; 
  update councilfullupdated set street = 'estcourt terrace' where fulladdress glob '*ESTCOURT TERRACE*'; 
  update councilfullupdated set street = 'grimthorpe street' where fulladdress glob '*GRIMTHORPE STREET*'; 
  update councilfullupdated set street = 'grimthorpe terrace' where fulladdress glob '*GRIMTHORPE TERRACE*'; 
  update councilfullupdated set street = 'headingley avenue' where fulladdress glob '*HEADINGLEY AVENUE*'; 
  update councilfullupdated set street = 'headingley mount' where fulladdress glob '*HEADINGLEY MOUNT*'; 
  update councilfullupdated set street = 'kirkstall lane' where fulladdress glob '*KIRKSTALL LANE*'; 
  update councilfullupdated set street = 'langdale avenue' where fulladdress glob '*LANGDALE AVENUEE*'; 
  update councilfullupdated set street = 'langdale gardens' where fulladdress glob '*LANGDAlE GARDENS*'; 
  update councilfullupdated set street = 'langdale avenue' where fulladdress glob '*LANGDALE AVENUE*'; 
  update councilfullupdated set street = 'langdale terrace' where fulladdress glob '*LANGDALE TERRACE*'; 
  update councilfullupdated set street = 'north lane' where fulladdress glob '*NORTH LANE*'; 
  update councilfullupdated set street = 'otley road' where fulladdress glob '*OTLEY ROAD*'; 
  update councilfullupdated set street = 'rokeby gardens' where fulladdress glob '*ROKEBY GARDENS*'; 
  update councilfullupdated set street = 'rokeby gardens' where fulladdress glob '*ST ANNES ROAD*'; 
  update councilfullupdated set street = 'st annes road' where fulladdress glob '*ST ANNES ROAD*'; 
  update councilfullupdated set street = 'trelawn avenue' where fulladdress glob '*TRELAWN AVENUE*'; 
  update councilfullupdated set street = 'trelawn crescent' where fulladdress glob '*TRELAWN CRESCENT*'; 
  update councilfullupdated set street = 'trelawn place' where fulladdress glob '*TRELAWN PLACE*'; 
  update councilfullupdated set street = 'trelawn street' where fulladdress glob '*TRELAWN STREET*'; 
  update councilfullupdated set street = 'winston gardens' where fulladdress glob '*WINSTON GARDENS*'; 
  update councilfullupdated set street = 'winston mount' where fulladdress glob '*WINSTON MOUNT*'; 
UPDATE councilfullupdated SET street = 'alexandra road' where fulladdress glob '*ALEXANDRA ROAD*';
UPDATE councilfullupdated SET street = 'alma cottages' where fulladdress glob '*ALMA COTTAGES*';
UPDATE councilfullupdated SET street = 'alma road' where fulladdress glob '*ALMA ROAD*';
UPDATE councilfullupdated SET street = 'ash avenue' where fulladdress glob '*ASH AVENUE*';
UPDATE councilfullupdated SET street = 'ash crescent' where fulladdress glob '*ASH CRESCENT*';
UPDATE councilfullupdated SET street = 'ashfield park' where fulladdress glob '*ASHFIELD PARK*';
UPDATE councilfullupdated SET street = 'ash view' where fulladdress glob '*ASH VIEW*';
UPDATE councilfullupdated SET street = 'ashville avenue' where fulladdress glob '*ASHVILLE AVENUE*';
UPDATE councilfullupdated SET street = 'ashville grove' where fulladdress glob '*ASHVILLE GROVE*';
UPDATE councilfullupdated SET street = 'ashville road' where fulladdress glob '*ASHVILLE ROAD*';
UPDATE councilfullupdated SET street = 'ashville terrace' where fulladdress glob '*ASHVILLE TERRACE*';
UPDATE councilfullupdated SET street = 'ashville view' where fulladdress glob '*ASHVILLE VIEW*';
UPDATE councilfullupdated SET street = 'ashwood terrace' where fulladdress glob '*ASHWOOD TERRACE*';
UPDATE councilfullupdated SET street = 'ashwood villas' where fulladdress glob '*ASHWOOD VILLAS*';
UPDATE councilfullupdated SET street = 'bainbrigge road' where fulladdress glob '*BAINBRIGGE ROAD*';
UPDATE councilfullupdated SET street = 'balbec avenue' where fulladdress glob '*BALBEC AVENUE*';
UPDATE councilfullupdated SET street = 'beamsley grove' where fulladdress glob '*BEAMSLEY GROVE*';
UPDATE councilfullupdated SET street = 'beamsley mount' where fulladdress glob '*BEAMSLEY MOUNT*';
UPDATE councilfullupdated SET street = 'beamsley place' where fulladdress glob '*BEAMSLEY PLACE*';
UPDATE councilfullupdated SET street = 'beamsley terrace' where fulladdress glob '*BEAMSLEY TERRACE*';
UPDATE councilfullupdated SET street = 'bennett road' where fulladdress glob '*BENNETT ROAD*';
UPDATE councilfullupdated SET street = 'branksome place' where fulladdress glob '*BRANKSOME PLACE*';
UPDATE councilfullupdated SET street = 'branksome terrace' where fulladdress glob '*BRANKSOME TERRACE*';
UPDATE councilfullupdated SET street = 'broomfield crescent' where fulladdress glob '*BROOMFIELD CRESCENT*';
UPDATE councilfullupdated SET street = 'broomfield place' where fulladdress glob '*BROOMFIELD PLACE*';
UPDATE councilfullupdated SET street = 'broomfield road' where fulladdress glob '*BROOMFIELD ROAD*';
UPDATE councilfullupdated SET street = 'broomfield terrace' where fulladdress glob '*BROOMFIELD TERRACE*';
UPDATE councilfullupdated SET street = 'broomfield view' where fulladdress glob '*BROOMFIELD VIEW*';
UPDATE councilfullupdated SET street = 'brudenell road' where fulladdress glob '*BRUDENELL ROAD*';
UPDATE councilfullupdated SET street = 'buckingham avenue' where fulladdress glob '*BUCKINGHAM AVENUE*';
UPDATE councilfullupdated SET street = 'buckingham drive' where fulladdress glob '*BUCKINGHAM DRIVE*';
UPDATE councilfullupdated SET street = 'buckingham grove' where fulladdress glob '*BUCKINGHAM GROVE*';
UPDATE councilfullupdated SET street = 'buckingham mount' where fulladdress glob '*BUCKINGHAM MOUNT*';
UPDATE councilfullupdated SET street = 'buckingham road' where fulladdress glob '*BUCKINGHAM ROAD*';
UPDATE councilfullupdated SET street = 'canterbury drive' where fulladdress glob '*CANTERBURY DRIVE*';
UPDATE councilfullupdated SET street = 'cardigan court' where fulladdress glob '*CARDIGAN COURT*';
UPDATE councilfullupdated SET street = 'cardigan lane' where fulladdress glob '*CARDIGAN LANE*';
UPDATE councilfullupdated SET street = 'cardigan road' where fulladdress glob '*CARDIGAN ROAD*';
UPDATE councilfullupdated SET street = 'chapel fold' where fulladdress glob '*CHAPEL FOLD*';
UPDATE councilfullupdated SET street = 'chapel lane' where fulladdress glob '*CHAPEL LANE*';
UPDATE councilfullupdated SET street = 'chapel place' where fulladdress glob '*CHAPEL PLACE*';
UPDATE councilfullupdated SET street = 'chapel square' where fulladdress glob '*CHAPEL SQUARE*';
UPDATE councilfullupdated SET street = 'chapel street' where fulladdress glob '*CHAPEL STREET*';
UPDATE councilfullupdated SET street = 'chestnut avenue' where fulladdress glob '*CHESTNUT AVENUE*';
UPDATE councilfullupdated SET street = 'chestnut grove' where fulladdress glob '*CHESTNUT GROVE*';
UPDATE councilfullupdated SET street = 'coniston avenue' where fulladdress glob '*CONISTON AVENUE*';
UPDATE councilfullupdated SET street = 'cumberland road' where fulladdress glob '*CUMBERLAND ROAD*';
UPDATE councilfullupdated SET street = 'elizabeth street' where fulladdress glob '*ELIZABETH STREET*';
UPDATE councilfullupdated SET street = 'granby avenue' where fulladdress glob '*GRANBY AVENUE*';
UPDATE councilfullupdated SET street = 'granby close' where fulladdress glob '*GRANBY CLOSE*';
UPDATE councilfullupdated SET street = 'granby grove' where fulladdress glob '*GRANBY GROVE*';
UPDATE councilfullupdated SET street = 'granby mount' where fulladdress glob '*GRANBY MOUNT*';
UPDATE councilfullupdated SET street = 'granby place' where fulladdress glob '*GRANBY PLACE*';
UPDATE councilfullupdated SET street = 'granby road' where fulladdress glob '*GRANBY ROAD*';
UPDATE councilfullupdated SET street = 'granby street' where fulladdress glob '*GRANBY STREET*';
UPDATE councilfullupdated SET street = 'granby terrace' where fulladdress glob '*GRANBY TERRACE*';
UPDATE councilfullupdated SET street = 'granby view' where fulladdress glob '*GRANBY VIEW*';
UPDATE councilfullupdated SET street = 'greyshiels avenue' where fulladdress glob '*GREYSHIELS AVENUE*';
UPDATE councilfullupdated SET street = 'greyshiels close' where fulladdress glob '*GREYSHIELS CLOSE*';
UPDATE councilfullupdated SET street = 'grimthorpe place' where fulladdress glob '*GRIMTHORPE PLACE*';
UPDATE councilfullupdated SET street = 'grosvenor mount' where fulladdress glob '*GROSVENOR MOUNT*';
UPDATE councilfullupdated SET street = 'grosvenor road' where fulladdress glob '*GROSVENOR ROAD*';
UPDATE councilfullupdated SET street = 'grosvenor terrace' where fulladdress glob '*GROSVENOR TERRACE*';
UPDATE councilfullupdated SET street = 'grove lane' where fulladdress glob '*GROVE LANE*';
UPDATE councilfullupdated SET street = 'grove road' where fulladdress glob '*GROVE ROAD*';
UPDATE councilfullupdated SET street = 'harold avenue' where fulladdress glob '*HAROLD AVENUE*';
UPDATE councilfullupdated SET street = 'harold grove' where fulladdress glob '*HAROLD GROVE*';
UPDATE councilfullupdated SET street = 'harold mount' where fulladdress glob '*HAROLD MOUNT*';
UPDATE councilfullupdated SET street = 'harold place' where fulladdress glob '*HAROLD PLACE*';
UPDATE councilfullupdated SET street = 'harold road' where fulladdress glob '*HAROLD ROAD*';
UPDATE councilfullupdated SET street = 'harold square' where fulladdress glob '*HAROLD SQUARE*';
UPDATE councilfullupdated SET street = 'harold street' where fulladdress glob '*HAROLD STREET*';
UPDATE councilfullupdated SET street = 'harold terrace' where fulladdress glob '*HAROLD TERRACE*';
UPDATE councilfullupdated SET street = 'harold view' where fulladdress glob '*HAROLD VIEW*';
UPDATE councilfullupdated SET street = 'harold walk' where fulladdress glob '*HAROLD WALK*';
UPDATE councilfullupdated SET street = 'headingley crescent' where fulladdress glob '*HEADINGLEY CRESCENT*';
UPDATE councilfullupdated SET street = 'headingley lane' where fulladdress glob '*HEADINGLEY LANE*';
UPDATE councilfullupdated SET street = 'headingley terrace' where fulladdress glob '*HEADINGLEY TERRACE*';
UPDATE councilfullupdated SET street = 'hessle avenue' where fulladdress glob '*HESSLE AVENUE*';
UPDATE councilfullupdated SET street = 'hessle mount' where fulladdress glob '*HESSLE MOUNT*';
UPDATE councilfullupdated SET street = 'hessle place' where fulladdress glob '*HESSLE PLACE*';
UPDATE councilfullupdated SET street = 'hessle road' where fulladdress glob '*HESSLE ROAD*';
UPDATE councilfullupdated SET street = 'hessle street' where fulladdress glob '*HESSLE STREET*';
UPDATE councilfullupdated SET street = 'hessle terrace' where fulladdress glob '*HESSLE TERRACE*';
UPDATE councilfullupdated SET street = 'hessle view' where fulladdress glob '*HESSLE VIEW*';
UPDATE councilfullupdated SET street = 'hessle walk' where fulladdress glob '*HESSLE WALK*';
UPDATE councilfullupdated SET street = 'hinsley court' where fulladdress glob '*HINSLEY COURT*';
UPDATE councilfullupdated SET street = 'hopewell place' where fulladdress glob '*HOPEWELL PLACE*';
UPDATE councilfullupdated SET street = 'john street' where fulladdress glob '*JOHN STREET*';
UPDATE councilfullupdated SET street = 'langdale gardens' where fulladdress glob '*LANGDALE GARDENS*';
UPDATE councilfullupdated SET street = 'manor avenue' where fulladdress glob '*MANOR AVENUE*';
UPDATE councilfullupdated SET street = 'manor drive' where fulladdress glob '*MANOR DRIVE*';
UPDATE councilfullupdated SET street = 'manor terrace' where fulladdress glob '*MANOR TERRACE*';
UPDATE councilfullupdated SET street = 'manor view' where fulladdress glob '*MANOR VIEW*';
UPDATE councilfullupdated SET street = 'mayville avenue' where fulladdress glob '*MAYVILLE AVENUE*';
UPDATE councilfullupdated SET street = 'mayville place' where fulladdress glob '*MAYVILLE PLACE*';
UPDATE councilfullupdated SET street = 'mayville road' where fulladdress glob '*MAYVILLE ROAD*';
UPDATE councilfullupdated SET street = 'mayville street' where fulladdress glob '*MAYVILLE STREET*';
UPDATE councilfullupdated SET street = 'mayville terrace' where fulladdress glob '*MAYVILLE TERRACE*';
UPDATE councilfullupdated SET street = 'meadow view' where fulladdress glob '*MEADOW VIEW*';
UPDATE councilfullupdated SET street = 'newport crescent' where fulladdress glob '*NEWPORT CRESCENT*';
UPDATE councilfullupdated SET street = 'newport gardens' where fulladdress glob '*NEWPORT GARDENS*';
UPDATE councilfullupdated SET street = 'newport mount' where fulladdress glob '*NEWPORT MOUNT*';
UPDATE councilfullupdated SET street = 'newport road' where fulladdress glob '*NEWPORT ROAD*';
UPDATE councilfullupdated SET street = 'newport view' where fulladdress glob '*NEWPORT VIEW*';
UPDATE councilfullupdated SET street = 'norville terrace' where fulladdress glob '*NORVILLE TERRACE*';
UPDATE councilfullupdated SET street = 'norwood grove' where fulladdress glob '*NORWOOD GROVE*';
UPDATE councilfullupdated SET street = 'norwood place' where fulladdress glob '*NORWOOD PLACE*';
UPDATE councilfullupdated SET street = 'norwood road' where fulladdress glob '*NORWOOD ROAD*';
UPDATE councilfullupdated SET street = 'norwood terrace' where fulladdress glob '*NORWOOD TERRACE*';
UPDATE councilfullupdated SET street = 'orville gardens' where fulladdress glob '*ORVILLE GARDENS*';
UPDATE councilfullupdated SET street = 'pearson avenue' where fulladdress glob '*PEARSON AVENUE*';
UPDATE councilfullupdated SET street = 'pearson grove' where fulladdress glob '*PEARSON GROVE*';
UPDATE councilfullupdated SET street = 'pearson terrace' where fulladdress glob '*PEARSON TERRACE*';
UPDATE councilfullupdated SET street = 'princes grove' where fulladdress glob '*PRINCE*S GROVE*';
UPDATE councilfullupdated SET street = 'queens road' where fulladdress glob '*QUEENS ROAD*';
UPDATE councilfullupdated SET street = 'raven road' where fulladdress glob '*RAVEN ROAD*';
UPDATE councilfullupdated SET street = 'richmond avenue' where fulladdress glob '*RICHMOND AVENUE*';
UPDATE councilfullupdated SET street = 'richmond mount' where fulladdress glob '*RICHMOND MOUNT*';
UPDATE councilfullupdated SET street = 'richmond road' where fulladdress glob '*RICHMOND ROAD*';
UPDATE councilfullupdated SET street = 'ridge terrace' where fulladdress glob '*RIDGE TERRACE*';
UPDATE councilfullupdated SET street = 'rochester terrace' where fulladdress glob '*ROCHESTER TERRACE*';
UPDATE councilfullupdated SET street = 'sagar place' where fulladdress glob '*SAGAR PLACE*';
UPDATE councilfullupdated SET street = 'school view' where fulladdress glob '*SCHOOL VIEW*';
UPDATE councilfullupdated SET street = 'south parade' where fulladdress glob '*SOUTH PARADE*';
UPDATE councilfullupdated SET street = 'spring road' where fulladdress glob '*SPRING ROAD*';
UPDATE councilfullupdated SET street = 'the poplars' where fulladdress glob '*THE POPLARS*';
UPDATE councilfullupdated SET street = 'the turnways' where fulladdress glob '*THE TURNWAYS*';
UPDATE councilfullupdated SET street = 'thornville avenue' where fulladdress glob '*THORNVILLE AVENUE*';
UPDATE councilfullupdated SET street = 'thornville crescent' where fulladdress glob '*THORNVILLE CRESCENT*';
UPDATE councilfullupdated SET street = 'thornville grove' where fulladdress glob '*THORNVILLE GROVE*';
UPDATE councilfullupdated SET street = 'thornville mount' where fulladdress glob '*THORNVILLE MOUNT*';
UPDATE councilfullupdated SET street = 'thornville place' where fulladdress glob '*THORNVILLE PLACE*';
UPDATE councilfullupdated SET street = 'thornville road' where fulladdress glob '*THORNVILLE ROAD*';
UPDATE councilfullupdated SET street = 'thornville row' where fulladdress glob '*THORNVILLE ROW*';
UPDATE councilfullupdated SET street = 'thornville street' where fulladdress glob '*THORNVILLE STREET*';
UPDATE councilfullupdated SET street = 'thornville terrace' where fulladdress glob '*THORNVILLE TERRACE*';
UPDATE councilfullupdated SET street = 'thornville view' where fulladdress glob '*THORNVILLE VIEW*';
UPDATE councilfullupdated SET street = 'trelawn terrace' where fulladdress glob '*TRELAWN TERRACE*';
UPDATE councilfullupdated SET street = 'trenic crescent' where fulladdress glob '*TRENIC CRESCENT*';
UPDATE councilfullupdated SET street = 'trenic drive' where fulladdress glob '*TRENIC DRIVE*';
UPDATE councilfullupdated SET street = 'victoria road' where fulladdress glob '*VICTORIA ROAD*';
UPDATE councilfullupdated SET street = 'walmsley road' where fulladdress glob '*WALMSLEY ROAD*';
UPDATE councilfullupdated SET street = 'wellfield place' where fulladdress glob '*WELLFIELD PLACE*';
UPDATE councilfullupdated SET street = 'welton grove' where fulladdress glob '*WELTON GROVE*';
UPDATE councilfullupdated SET street = 'welton mount' where fulladdress glob '*WELTON MOUNT*';
UPDATE councilfullupdated SET street = 'welton place' where fulladdress glob '*WELTON PLACE*';
UPDATE councilfullupdated SET street = 'welton road' where fulladdress glob '*WELTON ROAD*';
UPDATE councilfullupdated SET street = 'william street' where fulladdress glob '*WILLIAM STREET*';
UPDATE councilfullupdated SET street = 'winstanley terrace' where fulladdress glob '*WINSTANLEY TERRACE*';
UPDATE councilfullupdated SET street = 'wood lane' where fulladdress glob '*WOOD LANE*';
UPDATE councilfullupdated SET street = 'grimthorpe avenue' WHERE fulladdress GLOB '*GRIMTHORPE AVENUE*';
UPDATE councilfullupdated SET street = 'north hill road' WHERE fulladdress GLOB '*NORTH HILL ROAD*';
UPDATE councilfullupdated SET street = 'royal park road' WHERE fulladdress GLOB '*ROYAL PARK ROAD*';
UPDATE councilfullupdated SET street = 'shire oak road' WHERE fulladdress GLOB '*SHIRE OAK ROAD*';
UPDATE councilfullupdated SET street = 'shire oak street' WHERE fulladdress GLOB '*SHIRE OAK STREET*';
UPDATE councilfullupdated SET street = 'spring bank crescent' WHERE fulladdress GLOB '*SPRING BANK CRESCENT*';
UPDATE councilfullupdated SET street = 'spring grove view' WHERE fulladdress GLOB '*SPRING GROVE VIEW*';
UPDATE councilfullupdated SET street = 'spring grove walk' WHERE fulladdress GLOB '*SPRING GROVE WALK*';
UPDATE councilfullupdated SET street = 'st annes road' WHERE fulladdress GLOB '*ST ANNE*S ROAD*';
UPDATE councilfullupdated SET street = 'st michaels crescent' WHERE fulladdress GLOB '*ST MICHAEL*S CRESCENT*';
UPDATE councilfullupdated SET street = 'st michaels grove' WHERE fulladdress GLOB '*ST MICHAEL*S GROVE*';
UPDATE councilfullupdated SET street = 'st michaels lane' WHERE fulladdress GLOB '*ST MICHAEL*S LANE*';
UPDATE councilfullupdated SET street = 'st michaels road' WHERE fulladdress GLOB '*ST MICHAEL*S ROAD*';
UPDATE councilfullupdated SET street = 'st michaels terrace' WHERE fulladdress GLOB '*ST MICHAEL*S TERRACE*';
UPDATE councilfullupdated SET street = 'st michaels villas' WHERE fulladdress GLOB '*ST MICHAEL*S VILLA*';
UPDATE councilfullupdated SET street = 'woodland park road' WHERE fulladdress GLOB '*WOODLAND PARK ROAD*';

UPDATE councilfullupdated SET street = 'NORTH GRANGE ROAD' WHERE fulladdress GLOB '*NORTH GRANGE ROAD*';
UPDATE councilfullupdated SET street = 'BEAR PIT GARDENS' WHERE fulladdress GLOB '*BEAR PIT GARDENS*';
UPDATE councilfullupdated SET street = 'NORTH GRANGE MOUNT' WHERE fulladdress GLOB '*NORTH GRANGE MOUNT*';
UPDATE councilfullupdated SET street = 'NORTH GRANGE MEWS' WHERE fulladdress GLOB '*NORTH GRANGE MEWS*';
UPDATE councilfullupdated SET street = 'LAUREL BANK COURT' WHERE fulladdress GLOB '*LAUREL BANK COURT*';

UPDATE councilfullupdated SET street = 'LAUREL BANK COURT' WHERE fulladdress GLOB '*LAUREL BANK COURT*';

drop table toremove;
CREATE TABLE toremove(
  "pd" TEXT,
  "eno" TEXT,
  "firstname" TEXT,
  "surname" TEXT,
  "fulladdress" TEXT,
  "street" TEXT,
  "address_1" TEXT,
  "address_2" TEXT,
  "address_3" TEXT,
  "address_4" TEXT,
  "address_5" TEXT,
  "address_6" TEXT,
  "address_7" TEXT,
  "remove" text
);


insert into toremove (pd, eno, firstname, surname, address_1, address_2, address_3, address_4, address_5, address_6, address_7) select pd, eno, firstname, surname, address1, address2, address3, address4, address5, address6, address7
from council02 where remove is 'D';

insert into toremove (pd, eno, firstname, surname, address_1, address_2, address_3, address_4, address_5, address_6, address_7) select pd, eno, firstname, surname, address1, address2, address3, address4, address5, address6, address7
from council03 where remove is 'D';


UPDATE toremove SET remove = 'remove';


drop table draftfreshdata;
CREATE TABLE draftfreshdata(
  "pd" TEXT,
  "eno" TEXT,
  "firstname" TEXT,
  "surname" TEXT,
  "fulladdress" TEXT,
  "street" TEXT,
  "address_1" TEXT,
  "address_2" TEXT,
  "address_3" TEXT,
  "address_4" TEXT,
  "address_5" TEXT,
  "address_6" TEXT,
  "address_7" TEXT,
  "priorres" TEXT,
  "v12" TEXT,
  "v14" TEXT,
  "green" TEXT,
  "intent" TEXT,
  "surveyn" TEXT,
  "yearmovedin" TEXT,
  "knocked" TEXT,
  "other1" TEXT,
  "other2" TEXT,
  "partymember" TEXT
);

alter table old add column v12;
alter table old add column v14;
alter table old add column green;
alter table old add column intent;
alter table old add column surveyn;
alter table old add column knocked;
alter table old add column other1;
alter table old add column other2;
alter table old add column yearmovedin;
alter table old add column priorres;
alter table old add column partymember;
alter table members add column partymember;
alter table members add column street;


update old set priorres = 'yes'; 
update members set partymember = 'yes'; 



insert into draftfreshdata (pd,eno,firstname,surname,fulladdress,street,address_1,address_2,address_3,address_4,address_5,address_6,address_7,v12,v14,green,intent,surveyn,knocked,other1,other2,yearmovedin,priorres) 
select councilfullupdated.pd, councilfullupdated.eno, councilfullupdated.firstname, councilfullupdated.surname, councilfullupdated.fulladdress, councilfullupdated.street, councilfullupdated.address_1, councilfullupdated.address_2,councilfullupdated.address_3,councilfullupdated.address_4,councilfullupdated.address_5,councilfullupdated.address_6,councilfullupdated.address_7,
old.v12, old.v14, old.green, old.intent, old.surveyn, old.knocked, old.other1, old.other2, old.yearmovedin, old.priorres 
from councilfullupdated 
left outer join old on councilfullupdated.firstname = old.firstname and councilfullupdated.surname = old.surname and councilfullupdated.address_1 = old.address_1;

update draftfreshdata set yearmovedin = '2015' where priorres is not 'yes';
update draftfreshdata set priorres = 'no' where yearmovedin is '2015'; 

drop table streetmembers;
CREATE TABLE streetmembers(
  "FirstName" TEXT,
  "LastName" TEXT,
 partymember, street);

insert into streetmembers (FirstName, LastName, partymember, street) select draftfreshdata.firstname, draftfreshdata.surname, members.partymember, draftfreshdata.street from draftfreshdata inner join members on draftfreshdata.firstname = members.FirstName and draftfreshdata.surname = members.LastName and members.PostalCode = draftfreshdata.address_7;

insert into streetmembers (FirstName, LastName, partymember, street) select draftfreshdata.firstname, draftfreshdata.surname, members.partymember, draftfreshdata.street from draftfreshdata inner join members on draftfreshdata.firstname = members.FirstName and draftfreshdata.surname = members.LastName and members.PostalCode = draftfreshdata.address_6;
  
insert into streetmembers (FirstName, LastName, partymember, street) select draftfreshdata.firstname, draftfreshdata.surname, members.partymember, draftfreshdata.street from draftfreshdata inner join members on draftfreshdata.firstname = members.FirstName and draftfreshdata.surname = members.LastName and members.PostalCode = draftfreshdata.address_5;

insert into streetmembers (FirstName, LastName, partymember, street) select draftfreshdata.firstname, draftfreshdata.surname, members.partymember, draftfreshdata.street from draftfreshdata inner join members on draftfreshdata.firstname = members.FirstName and draftfreshdata.surname = members.LastName and members.PostalCode = draftfreshdata.address_4;

insert into streetmembers (FirstName, LastName, partymember, street) select draftfreshdata.firstname, draftfreshdata.surname, members.partymember, draftfreshdata.street from draftfreshdata inner join members on draftfreshdata.firstname = members.FirstName and draftfreshdata.surname = members.LastName and members.PostalCode = draftfreshdata.address_3;

insert into streetmembers (FirstName, LastName, partymember, street) select draftfreshdata.firstname, draftfreshdata.surname, members.partymember, draftfreshdata.street from draftfreshdata inner join members on draftfreshdata.firstname = members.FirstName and draftfreshdata.surname = members.LastName and members.PostalCode = draftfreshdata.address_2;

insert into streetmembers (FirstName, LastName, partymember, street) select draftfreshdata.firstname, draftfreshdata.surname, members.partymember, draftfreshdata.street from draftfreshdata inner join members on draftfreshdata.firstname = members.FirstName and draftfreshdata.surname = members.LastName and members.PostalCode = draftfreshdata.address_1;

drop table cleandata;
CREATE TABLE cleandata(
  "pd" TEXT,
  "eno" TEXT,
  "firstname" TEXT,
  "surname" TEXT,
  "fulladdress" TEXT,
  "street" TEXT,
  "address_1" TEXT,
  "address_2" TEXT,
  "address_3" TEXT,
  "address_4" TEXT,
  "address_5" TEXT,
  "address_6" TEXT,
  "address_7" TEXT,
  "priorres" TEXT,
  "v12" TEXT,
  "v14" TEXT,
  "green" TEXT,
  "intent" TEXT,
  "surveyn" TEXT,
  "yearmovedin" TEXT,
  "knocked" TEXT,
  "other1" TEXT,
  "other2" TEXT,
  "partymember" TEXT,
  "remove"
);

insert into cleandata (pd, eno, firstname, surname, fulladdress, street, address_1, address_2, address_3, address_4, address_5, address_6, address_7, priorres, v12, v14, green, intent, surveyn, knocked, other1, other2, yearmovedin, remove) 
select draftfreshdata.pd, draftfreshdata.eno, draftfreshdata.firstname, draftfreshdata.surname, draftfreshdata.fulladdress, draftfreshdata.street, draftfreshdata.address_1, draftfreshdata.address_2, draftfreshdata.address_3, draftfreshdata.address_4, draftfreshdata.address_5, draftfreshdata.address_6, draftfreshdata.address_7, draftfreshdata.priorres, draftfreshdata.v12, draftfreshdata.v14, draftfreshdata.green, draftfreshdata.intent, draftfreshdata.surveyn, draftfreshdata.knocked, draftfreshdata.other1, draftfreshdata.other2, draftfreshdata.yearmovedin, toremove.remove
from draftfreshdata left outer join toremove on draftfreshdata.firstname = toremove.firstname and draftfreshdata.surname = toremove.surname and draftfreshdata.address_1 = toremove.address_1;

drop table freshdata;
CREATE TABLE freshdata(
  "pd" TEXT,
  "eno" TEXT,
  "firstname" TEXT,
  "surname" TEXT,
  "fulladdress" TEXT,
  "street" TEXT,
  "address_1" TEXT,
  "address_2" TEXT,
  "address_3" TEXT,
  "address_4" TEXT,
  "address_5" TEXT,
  "address_6" TEXT,
  "address_7" TEXT,
  "priorres" TEXT,
  "v12" TEXT,
  "v14" TEXT,
  "green" TEXT,
  "intent" TEXT,
  "surveyn" TEXT,
  "yearmovedin" TEXT,
  "knocked" TEXT,
  "other1" TEXT,
  "other2" TEXT,
  "partymember" TEXT,
  "remove"
);

insert into freshdata (pd, eno, firstname, surname, fulladdress, street, address_1, address_2, address_3, address_4, address_5, address_6, address_7, priorres, v12, v14, green, intent, surveyn, knocked, other1, other2, yearmovedin, partymember, remove) 
select cleandata.pd, cleandata.eno, cleandata.firstname, cleandata.surname, cleandata.fulladdress, cleandata.street, cleandata.address_1, cleandata.address_2, cleandata.address_3, cleandata.address_4, cleandata.address_5, cleandata.address_6, cleandata.address_7, cleandata.priorres, cleandata.v12, cleandata.v14, cleandata.green, cleandata.intent, cleandata.surveyn, cleandata.knocked, cleandata.other1, cleandata.other2, cleandata.yearmovedin, streetmembers.partymember, cleandata.remove
from cleandata left outer join streetmembers on cleandata.firstname = streetmembers.FirstName and cleandata.surname = streetmembers.Lastname and cleandata.street = streetmembers.street;

drop table streetdatares;
drop table streetdatav14;
drop table streetdatav14k;
drop table streetdatav14notk;
drop table togetherstreet;
drop table streetdatagreen45;
drop table streetdatagreen45v14;
drop table streetdatak;


create table streetdatares (street, res);
insert into streetdatares (street, res) select distinct street, count (eno) from freshdata group by street;
create table streetdatav14 (street, v14);
insert into streetdatav14 (street, v14) select distinct street, count (v14) from freshdata where v14 is 'x' group by street;
create table streetdatav14k (street, v14k);
insert into streetdatav14k (street, v14k) select distinct street, count (v14) from freshdata where v14 is 'x' and knocked is not '' group by street;
create table streetdatav14notk (street, v14notk);
insert into streetdatav14notk (street, v14notk) select distinct street, count (v14) from freshdata where v14 is 'x' and knocked is '' group by street;

create table streetdatagreen45 (street, green45);
insert into streetdatagreen45 (street, green45) select distinct street, count (eno) from freshdata where green >= 4 group by street;

create table streetdatagreen45v14 (street, green45v14);
insert into streetdatagreen45v14 (street, green45v14) select distinct street, count (eno) from freshdata where green >= 4 and v14 is 'x' group by street;

create table streetdatak (street, k);
insert into streetdatak (street, k) select distinct street, count (eno) from freshdata where knocked is NULL group by street;

create table togetherstreet (street, res, k, v14, v14k, v14notk, green45, green45v14);

insert into togetherstreet (street, res, k, v14, v14k, v14notk, green45, green45v14) select streetdatares.street, streetdatares.res, streetdatak.k, streetdatav14.v14, streetdatav14k.v14k, streetdatav14notk.v14notk, streetdatagreen45.green45, streetdatagreen45v14.green45v14 from streetdatares left outer join streetdatav14 on streetdatares.street = streetdatav14.street left outer join streetdatav14k on streetdatares.street = streetdatav14k.street left outer join streetdatav14notk on streetdatares.street = streetdatav14notk.street left outer join streetdatagreen45 on streetdatares.street = streetdatagreen45.street left outer join streetdatagreen45v14 on streetdatares.street = streetdatagreen45v14.street left outer join streetdatak on streetdatares.street = streetdatak.street;

drop table pddatares;
drop table pddatav14;
drop table pddatav14k;
drop table pddatav14notk;
drop table togetherpd;
drop table pddatagreen45;
drop table pddatagreen45v14;
drop table pddatak;


create table pddatares (pd, res);
insert into pddatares (pd, res) select distinct pd, count (eno) from freshdata group by pd;
create table pddatav14 (pd, v14);
insert into pddatav14 (pd, v14) select distinct pd, count (v14) from freshdata where v14 is 'x' group by pd;
create table pddatav14k (pd, v14k);
insert into pddatav14k (pd, v14k) select distinct pd, count (v14) from freshdata where v14 is 'x' and knocked is not '' group by pd;
create table pddatav14notk (pd, v14notk);
insert into pddatav14notk (pd, v14notk) select distinct pd, count (v14) from freshdata where v14 is 'x' and knocked is '' group by pd;

create table pddatagreen45 (pd, green45);
insert into pddatagreen45 (pd, green45) select distinct pd, count (eno) from freshdata where green >= 4 group by pd;

create table pddatagreen45v14 (pd, green45v14);
insert into pddatagreen45v14 (pd, green45v14) select distinct pd, count (eno) from freshdata where green >= 4 and v14 is 'x' group by pd;

create table pddatak (pd, k);
insert into pddatak (pd, k) select distinct pd, count (eno) from freshdata where knocked is null group by pd;



create table togetherpd (pd, res, k, v14, v14k, v14notk, green45, green45v14);

insert into togetherpd (pd, res, k, v14, v14k, v14notk, green45, green45v14) select pddatares.pd, pddatares.res, pddatak.k, pddatav14.v14, pddatav14k.v14k, pddatav14notk.v14notk, pddatagreen45.green45, pddatagreen45v14.green45v14 from pddatares left outer join pddatav14 on pddatares.pd = pddatav14.pd left outer join pddatav14k on pddatares.pd = pddatav14k.pd left outer join pddatav14notk on pddatares.pd = pddatav14notk.pd left outer join pddatagreen45 on pddatares.pd = pddatagreen45.pd left outer join pddatagreen45v14 on pddatares.pd = pddatagreen45v14.pd left outer join pddatak on pddatares.pd = pddatak.pd;

.headers on
.output 1newdata.csv
select * from freshdata;
.output stdout

.output 1pddata.csv
select * from togetherpd;
.output stdout

.output 1streetdata.csv
select * from togetherstreet; 
.output stdout

drop table freshdata;
drop table pddatares;
drop table pddatav14;
drop table pddatav14k;
drop table togetherpd;
drop table pddatagreen45;
drop table pddatagreen45v14;
drop table pddatak;
drop table streetdatares;
drop table streetdatav14;
drop table streetdatav14k;
drop table togetherstreet;
drop table streetdatagreen45;
drop table streetdatagreen45v14;
drop table streetdatak;

.mode csv
.import 1newdata.csv freshdata

create table pddatares (pd, res);
insert into pddatares (pd, res) select distinct pd, count (eno) from freshdata group by pd;
create table pddatav14 (pd, v14);
insert into pddatav14 (pd, v14) select distinct pd, count (v14) from freshdata where v14 is 'x' group by pd;
create table pddatav14k (pd, v14k);
insert into pddatav14k (pd, v14k) select distinct pd, count (v14) from freshdata where v14 is 'x' and knocked is not '' group by pd;

create table pddatagreen45 (pd, green45);
insert into pddatagreen45 (pd, green45) select distinct pd, count (eno) from freshdata where green >= 4 group by pd;

create table pddatagreen45v14 (pd, green45v14);
insert into pddatagreen45v14 (pd, green45v14) select distinct pd, count (eno) from freshdata where green >= 4 and v14 is 'x' group by pd;

create table pddatak (pd, k);
insert into pddatak (pd, k) select distinct pd, count (eno) from freshdata where knocked is not '' group by pd;

create table togetherpd (pd, res, k, v14, v14k, green45, green45v14, rk, rv14, rv14k, rgreen45, rgreen45v14);

insert into togetherpd (pd, res, k, v14, v14k, green45, green45v14, rk, rv14, rv14k, rgreen45, rgreen45v14) select pddatares.pd, pddatares.res, pddatak.k, pddatav14.v14, pddatav14k.v14k, pddatagreen45.green45, pddatagreen45v14.green45v14, pddatak.k*100/pddatares.res, pddatav14.v14*100/pddatares.res, pddatav14k.v14k*100/pddatares.res, pddatagreen45.green45*100/pddatares.res, pddatagreen45v14.green45v14*100/pddatares.res from pddatares left outer join pddatav14 on pddatares.pd = pddatav14.pd left outer join pddatav14k on pddatares.pd = pddatav14k.pd left outer join pddatagreen45 on pddatares.pd = pddatagreen45.pd left outer join pddatagreen45v14 on pddatares.pd = pddatagreen45v14.pd left outer join pddatak on pddatares.pd = pddatak.pd;

create table streetdatares (street, res, pd);
insert into streetdatares (street, res, pd) select distinct street, count (eno), pd from freshdata group by street;
create table streetdatav14 (street, v14);
insert into streetdatav14 (street, v14) select distinct street, count (v14) from freshdata where v14 is 'x' group by street;
create table streetdatav14k (street, v14k);
insert into streetdatav14k (street, v14k) select distinct street, count (v14) from freshdata where v14 is 'x' and knocked is not '' group by street;

create table streetdatagreen45 (street, green45);
insert into streetdatagreen45 (street, green45) select distinct street, count (eno) from freshdata where green >= 4 group by street;

create table streetdatagreen45v14 (street, green45v14);
insert into streetdatagreen45v14 (street, green45v14) select distinct street, count (eno) from freshdata where green >= 4 and v14 is 'x' group by street;

create table streetdatak (street, k);
insert into streetdatak (street, k) select distinct street, count (eno) from freshdata where knocked is not '' group by street;



create table togetherstreet (pd, street, res, k, v14, v14k, green45, green45v14, rk, rv14, rv14k, rgreen45, rgreen45v14);

insert into togetherstreet (pd, street, res, k, v14, v14k, green45, green45v14, rk, rv14, rv14k, rgreen45, rgreen45v14) select streetdatares.pd, streetdatares.street, streetdatares.res, streetdatak.k, streetdatav14.v14, streetdatav14k.v14k, streetdatagreen45.green45, streetdatagreen45v14.green45v14, streetdatak.k*100/streetdatares.res, streetdatav14.v14*100/streetdatares.res, streetdatav14k.v14k*100/streetdatares.res, streetdatagreen45.green45*100/streetdatares.res, streetdatagreen45v14.green45v14*100/streetdatares.res from streetdatares left outer join streetdatav14 on streetdatares.street = streetdatav14.street left outer join streetdatav14k on streetdatares.street = streetdatav14k.street left outer join streetdatagreen45 on streetdatares.street = streetdatagreen45.street left outer join streetdatagreen45v14 on streetdatares.street = streetdatagreen45v14.street left outer join streetdatak on streetdatares.street = streetdatak.street;


.headers on
.output 1streetdata.csv
select * from togetherstreet;
.output stdout


.headers on
.output 1pddata.csv
select * from togetherpd;
.output stdout




drop table pdknocknext;
create table pdknocknext (pd);

insert into pdknocknext (pd) select pd from togetherpd order by rk limit 1;

drop table streetknocknext1;
create table streetknocknext1 (pd, street, rk, rv14, rgreen45);

insert into streetknocknext1 (pd, street, rk, rv14, rgreen45) select pdknocknext.pd, togetherstreet.street, togetherstreet.rk, togetherstreet.rv14, togetherstreet.rgreen45 from togetherstreet inner join pdknocknext on pdknocknext.pd = togetherstreet.pd;
 
drop table streetknocknext2;
create table streetknocknext2 (pd, street, rk, rv14, rgreen45);

insert into streetknocknext2 (pd, street, rk, rv14, rgreen45) select pd, street, rk, rv14, rgreen45 from streetknocknext1 order by rk limit 40;

drop table streetknocknext3;
create table streetknocknext3 (pd, street, rk, rv14, rgreen45);

insert into streetknocknext3 (pd, street, rk, rv14, rgreen45) select pd, street, rk, rv14, rgreen45 from streetknocknext1 order by rv14 desc limit 30;

drop table streetknocknext;
create table streetknocknext (pd, street, rk, rv14, rgreen45);

insert into streetknocknext (pd, street, rk, rv14, rgreen45) select pd, street, rk, rv14, rgreen45 from streetknocknext1 order by rgreen45 desc limit 20;

drop table knockdraft;

create table knockdraft (
  "pd" TEXT,
  "eno" TEXT,
  "firstname" TEXT,
  "surname" TEXT,
  "fulladdress" TEXT,
  "street" TEXT,
  "address_1" TEXT,
  "address_2" TEXT,
  "address_3" TEXT,
  "address_4" TEXT,
  "address_5" TEXT,
  "address_6" TEXT,
  "address_7" TEXT,
  "priorres" TEXT,
  "v12" TEXT,
  "v14" TEXT,
  "green" TEXT,
  "intent" TEXT,
  "surveyn" TEXT,
  "yearmovedin" TEXT,
  "knocked" TEXT,
  "other1" TEXT,
  "other2" TEXT
);

insert into knockdraft (pd, eno, firstname, surname, fulladdress, street, address_1, address_2, address_3, address_4, address_5, address_6, address_7, priorres, v12, v14, green, intent, surveyn, yearmovedin, knocked, other1, other2) select streetknocknext.pd, freshdata.eno, freshdata.firstname, freshdata.surname, freshdata.fulladdress, streetknocknext.street, freshdata.address_1, freshdata.address_2, freshdata.address_3, freshdata.address_4, freshdata.address_5, freshdata.address_6, freshdata.address_7, freshdata.priorres, freshdata.v12, freshdata.v14, freshdata.green, freshdata.intent, freshdata.surveyn, freshdata.yearmovedin, freshdata.knocked, freshdata.other1, freshdata.other2 from freshdata inner join streetknocknext on streetknocknext.street = freshdata.street;

drop table knock;
create table knock (
  "firstname" TEXT,
  "surname" TEXT,
  "fulladdress" TEXT,
  "street" TEXT,
  "address_1" TEXT,
  "priorres" TEXT,
  "v12" TEXT,
  "v14" TEXT,
  "green" TEXT,
  "intent" TEXT,
  "surveyn" TEXT,
  "yearmovedin" TEXT,
  "knocked" TEXT,
  "other1" TEXT,
  "other2" TEXT
);

insert into knock (firstname, surname, fulladdress, street, address_1, priorres, v12, v14, green, intent, surveyn, yearmovedin, knocked, other1, other2) select firstname, surname, fulladdress, street, address_1, priorres, v12, v14, green, intent, surveyn, yearmovedin, knocked, other1, other2 from knockdraft order by street;

.output 1knockdraft.csv
select * from knockdraft;
.output stdout

.output 1knock.csv
select * from knock;
.output stdout


