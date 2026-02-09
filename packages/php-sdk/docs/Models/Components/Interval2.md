# Interval2


## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `day`                                                         | *?string*                                                     | :heavy_minus_sign:                                            | Day of week (e.g., Monday, Tuesday).                          |
| `date`                                                        | [\DateTime](https://www.php.net/manual/en/class.datetime.php) | :heavy_check_mark:                                            | Calendar date in YYYY-MM-DD.                                  |
| `fromHour`                                                    | *int*                                                         | :heavy_check_mark:                                            | Start hour (0-23).                                            |
| `fromMinute`                                                  | *int*                                                         | :heavy_check_mark:                                            | Start minute (0-59).                                          |
| `toHour`                                                      | *int*                                                         | :heavy_check_mark:                                            | End hour (0-23).                                              |
| `toMinute`                                                    | *int*                                                         | :heavy_check_mark:                                            | End minute (0-59).                                            |