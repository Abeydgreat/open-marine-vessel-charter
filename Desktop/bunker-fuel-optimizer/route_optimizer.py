import argparse

def optimize_voyage(distance_nm, current_fuel_price_usd, base_speed_knots=16.0):
    eco_speed_knots = 12.0
    base_daily_consumption = 35.0 
    eco_daily_consumption = base_daily_consumption * ((eco_speed_knots / base_speed_knots) ** 3)
    base_hours = distance_nm / base_speed_knots
    eco_hours = distance_nm / eco_speed_knots
    base_days = base_hours / 24.0
    eco_days = eco_hours / 24.0
    base_total_fuel = base_days * base_daily_consumption
    eco_total_fuel = eco_days * eco_daily_consumption
    base_cost = base_total_fuel * current_fuel_price_usd
    eco_cost = eco_total_fuel * current_fuel_price_usd
    total_savings = base_cost - eco_cost
    
    print("=" * 60)
    print(f"🚢 OMVC ECO-STEAMING MARINE OPTIMIZATION ENGINE")
    print("=" * 60)
    print(f"Voyage Distance            : {distance_nm:,} Nautical Miles")
    print(f"Current Marine Fuel Price  : ${current_fuel_price_usd:,.2f} / Metric Ton")
    print("-" * 60)
    print(f"[STANDARD ROUTE] Fuel Cost: ${base_cost:,.2f}")
    print(f"[OPTIMIZED ROUTE] Fuel Cost: ${eco_cost:,.2f}")
    print("-" * 60)
    print(f"🔥 PROJECTED INVESTOR FUEL COST SAVINGS: ${total_savings:,.2f}")
    print("=" * 60)
    return total_savings

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--distance", type=float, default=3000.0)
    parser.add_argument("--fuel_price", type=float, default=650.0)
    args = parser.parse_args()
    optimize_voyage(args.distance, args.fuel_price)
