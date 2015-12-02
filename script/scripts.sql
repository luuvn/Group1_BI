CREATE TABLE VNE_LOG(
Id VARCHAR(100),
ACCESS_TIME VARCHAR(100),
SESSION_ID VARCHAR(100),
URL VARCHAR(max),
SCREEN_RESOLUTION VARCHAR(150),
BROWSER VARCHAR(100),
OS VARCHAR(100),
DEVICE_TYPE VARCHAR(100),
DEVICE_NAME VARCHAR(255),
IP_ADDRESS VARCHAR(50),
FROM_URL VARCHAR(max)
);

---------------------DIM_DEVICE---------------------
create table DimDevice
(
	ID int IDENTITY PRIMARY KEY nonclustered,
	DEVICE_NAME nvarchar(255) not null,
	DEVICE_TYPE nvarchar(100) not null,
	SCREEN_RESOLUTION nvarchar(100) not null
);
INSERT INTO dbo.DimDevice(SCREEN_RESOLUTION, DEVICE_NAME, DEVICE_TYPE)
(select SCREEN_RESOLUTION, DEVICE_NAME, DEVICE_TYPE from VNE_LOG group by SCREEN_RESOLUTION, DEVICE_NAME, DEVICE_TYPE)
------------------------------------------------------

---------------------DIM_DATE---------------------
create table DimDate
(
	ID int IDENTITY PRIMARY KEY nonclustered,
	DateAltKey VARCHAR(100) not null,
	CalendarYear int not null,
	CalendarQuarter int not null,
	MonthOfYear int not null,
	[MonthName] nvarchar(15) not null,
	[DayOfMonth] int not null,
	[DayOfWeek] int not null,
	[DayName] nvarchar(15) not null
);
 ---------------------------------------------------

 ---------------------DIM_BROWSER---------------------
 create table DimBrowser
(
	ID int IDENTITY PRIMARY KEY nonclustered,
	BROWSER_NAME nvarchar(50) not null
);
------------------------------------------------------


----------------------DIM_OS------------------------------- 
 create table DimOS
(
	ID int IDENTITY PRIMARY KEY nonclustered,
	OS_NAME nvarchar(50) not null
);
-----------------------------------------------------------

-----------------------DIM_CATEGORY------------------------
 create table DimCategory
(
	ID int IDENTITY PRIMARY KEY nonclustered,
	CATEGORY_NAME nvarchar(20) not null
);
INSERT INTO DimCategory(CATEGORY_NAME) values(N'Thời sự')
INSERT INTO DimCategory(CATEGORY_NAME) values(N'Thế giới')
INSERT INTO DimCategory(CATEGORY_NAME) values(N'Kinh doanh')
INSERT INTO DimCategory(CATEGORY_NAME) values(N'Giải trí')
INSERT INTO DimCategory(CATEGORY_NAME) values(N'Thể thao')
INSERT INTO DimCategory(CATEGORY_NAME) values(N'Pháp luật')
INSERT INTO DimCategory(CATEGORY_NAME) values(N'Gia đình')
INSERT INTO DimCategory(CATEGORY_NAME) values(N'Du lịch')
INSERT INTO DimCategory(CATEGORY_NAME) values(N'Khoa học')
INSERT INTO DimCategory(CATEGORY_NAME) values(N'Số hóa')
INSERT INTO DimCategory(CATEGORY_NAME) values(N'Xe')
INSERT INTO DimCategory(CATEGORY_NAME) values(N'Cộng đồng')
INSERT INTO DimCategory(CATEGORY_NAME) values(N'Tâm sự')
INSERT INTO DimCategory(CATEGORY_NAME) values(N'Video')
INSERT INTO DimCategory(CATEGORY_NAME) values(N'Cười')
INSERT INTO DimCategory(CATEGORY_NAME) values(N'Rao vặt')
INSERT INTO DimCategory(CATEGORY_NAME) values(N'ngoisao.net')
INSERT INTO DimCategory(CATEGORY_NAME) values(N'nhacso.net')
INSERT INTO DimCategory(CATEGORY_NAME) values(N'vitalk.vn')
INSERT INTO DimCategory(CATEGORY_NAME) values(N'ione')
INSERT INTO DimCategory(CATEGORY_NAME) values(N'game')
INSERT INTO DimCategory(CATEGORY_NAME) values(N'sendo.vn')
INSERT INTO DimCategory(CATEGORY_NAME) values(N'Homepage')
INSERT INTO DimCategory(CATEGORY_NAME) values(N'Đời sống')
INSERT INTO DimCategory(CATEGORY_NAME) values(N'Tin tức')
INSERT INTO DimCategory(CATEGORY_NAME) values(N'Others')
-----------------------------------------------------------

create table FactAccessCount
(
	DeviceID int not null references DimDevice(ID),
	DateID int not null references DimDate(ID),
	BrowserID int not null references DimBrowser(ID),
	OsID int not null references DimOS(ID),
	CategoryID int not null references DimCategory(ID),
	NUM_OF_ACCESS int not null,
	constraint [PK_FactAccessCount] primary key nonclustered
	(
		[DeviceID], [DateID], [BrowserID], [OsID], [CategoryID]
	)
)
GO
------------------------------------------------------------------
