# API

Meta information about API


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `added`                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Timestamp when the API was first added to the directory              |
| `preferred`                                                          | *str*                                                                | :heavy_check_mark:                                                   | Recommended version                                                  |
| `versions`                                                           | dict[str, [APIVersion](../../models/shared/apiversion.md)]           | :heavy_check_mark:                                                   | List of supported versions of the API                                |