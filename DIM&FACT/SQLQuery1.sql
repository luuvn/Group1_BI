--Fact: NumberOfAccess
USE VNELOG
GO

create table DimUser
(
	UserID int identity not null primary key nonclustered,
	UserIP nvarchar(50) not null
)
GO

create table DimDevice
(
	DeviceID int identity not null primary key nonclustered,
	DeviceResolution nvarchar(50) not null,
	Browser nvarchar(50) not null,
	OperatingSystem nvarchar(50) not null,
	DeviceType nvarchar(50) not null
)
GO

create table DimDate
(
	DateKey int not null primary key nonclustered,
	DateAltKey datetime not null,
	CalendarYear int not null,
	CalendarQuarter int not null,
	MonthOfYear int not null,
	[MonthName] nvarchar(15) not null,
	[DayOfMonth] int not null,
	[DayOfWeek] int not null,
	[DayName] nvarchar(15) not null
)
GO

--Create Fact table

create table FactUserAccess
(
	UserID int not null references DimUser(UserID),
	DeviceID int not null references DimDevice(DeviceID),
	DateKey int not null references DimDate(DateKey),
	UserNo int not null,
	BrowserNo int not null,
	OperatingSystemNo int not null,
	DeviceTypeNo int not null,
	constraint [PK_FactUserAccess] primary key nonclustered
	(
		[UserID], [DeviceID], [DateKey]
	)
)
GO

--Try to insert data
declare @date datetime
set @date = '2014-01-30 15:19:47.000'
insert into DimDate values
(
	CAST(convert(varchar(8), @date, 112) AS INT), -- date key
	@date, --date in string
	YEAR(@date), --calendar year
	DATEPART(QQ, @date), --calendar quarter
	Month(@date), --month of year
	DATENAME(MM, @date), --month name
	DAY(@date),
	DATEPART(DW, @date), --day of week
	DATEName(DW, @date) --day name of week
)

select * from DimDate

select * from HistoricalAccessSample

--create view
create view [DIM User] as
	select ROW_NUMBER() OVER (ORDER BY id) AS UserID,
	IP_ADDRESS from HistoricalAccessSample

select * from [DIM User]

create view [DIM Device] as
	select ROW_NUMBER() OVER (ORDER BY id, BROWSER) AS DeviceID,
	SCREEN_RESOLUTION, BROWSER, OS, DEVICE_TYPE from HistoricalAccessSample

select * from [DIM Device]

create view [DIM Date] as
	select CAST(convert(varchar(8), ACCESS_TIME, 112) AS INT) AS DateKey, -- date key
		ACCESS_TIME AS DateAltKey, --date in string
		YEAR(ACCESS_TIME) AS CalendarYear, --calendar year
		DATEPART(QQ, ACCESS_TIME) AS CalendarQuarter, --calendar quarter
		Month(ACCESS_TIME) AS MonthOfYear, --month of year
		DATENAME(MM, ACCESS_TIME) AS [MonthName], --month name
		DAY(ACCESS_TIME) AS [DayOfMonth],
		DATEPART(DW, ACCESS_TIME) AS [DayOfWeek], --day of week
		DATEName(DW, ACCESS_TIME) AS [DayName] --day name of week
	from HistoricalAccessSample

select * from [DIM Date]
