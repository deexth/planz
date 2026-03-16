# planz.com
Dashboard with plannings(whatto buy, travels, etc..), todos, and expense tracker
https://tequila.kiwi.com/portal/getting-started

apis:

-   **amadeus travel api**
    -   hotel search
    -   hotel offers
    -   flight search
-   **google places api**
    -   restaurants
    -   attractions
    -   points of interest
-   **openstreetmap / mapbox**
    -   maps
    -   geolocation

-------------------------------------

 Frontend (Flutter / Web)
            |
            |
          py API
            |
            |
      External Travel APIs
     (Amadeus / Expedia etc.)
------------------------------------

**Frontend** - Dashboard UI - Trip planner - Todo lists - Expense
tracker - Hotel browsing

**Backend (py API)** - User authentication - Trip management - Expense
tracking - API aggregation - Caching results from travel APIs

**External APIs** - Hotels - Flights - Location information

------------------------------------
Example structure for the dashboard features:

    User Dashboard
    │
    ├── Trips
    │   ├── Hotels API
    │   ├── Flights API
    │   └── Activities
    │
    ├── Todo Lists
    │
    ├── Expense Tracker
    │
    └── Travel Budget

------------------------------------
## Example Travel Flow

    Search city
       ↓
    Fetch hotels from travel API
       ↓
    Display available rooms
       ↓
    User saves hotel to trip plan
       ↓
    Expense gets added to travel budget

------------------------------------------------------------------------

## Key Design Idea

combines:

-   Trip planning
-   Budget tracking
-   Todos
-   Hotel and flight discovery
-   Personal travel organization

Example:

    Trip: Tokyo

    Budget: $2000

    Hotel: $800
    Flights: $700
    Food estimate: $300

    Remaining: $200

