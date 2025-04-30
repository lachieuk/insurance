import streamlit as st

# Lachie Insurance Testing App
def calculate_premium(base_premium, customer_data):
    # Factor definitions
    age_factor = {
        17: 15, 18: 14.5, 19: 14, 20: 13.9, 21: 10, 22: 7, 23: 5, 24: 3.5, 25: 2.5,
        26: 1.5, 27: 1.3, 28: 1.2, 29: 1.1, 30: 1, 31: 1, 32: 1, 33: 1, 34: 1, 35: 1,
        36: 1, 37: 1, 38: 1, 39: 1, 40: 0.8, 41: 0.8, 42: 0.8, 43: 0.8, 44: 0.8, 45: 0.8,
        46: 0.8, 47: 0.8, 48: 0.8, 49: 0.8, 50: 0.85, 51: 0.85, 52: 0.85, 53: 0.85, 54: 0.85,
        55: 0.85, 56: 0.85, 57: 0.85, 58: 0.85, 59: 0.85, 60: 0.9
    }
    driving_experience_factor = {
        '<2': 1.2, '2-5': 1.1, '5-10': 1, '10-20': 0.9, '>20': 0.85
    }
    driving_record_factor = {
        'Clean Record': 1, '1 Minor Violation': 1.2, '2 Minor Violations': 1.4,
        '1 Major Violation': 2, '1 At-Fault Claim': 1.4, '2 At-Fault Claims': 1.8,
        '1 Minor + 1 At-Fault': 1.6, '1 Major + 1 At-Fault': 2.5, 'Multiple Violations/Claims': 3
    }
    no_claims_discount_factor = {
        0: 1, 1: 0.9, 2: 0.85, 3: 0.8, 4: 0.75, 5: 0.7, 6: 0.65, 7: 0.6, 8: 0.55, 9: 0.5
    }
    location_factor = {
        'Central London': 1.5, 'Outer London': 1.3, 'Birmingham': 1.25, 'Manchester': 1,
        'Leeds': 1.05, 'Glasgow': 1.15, 'Liverpool': 1.2, 'Newcastle': 1, 'Sheffield': 1.05,
        'Bristol': 1, 'Edinburgh': 0.9, 'Cardiff': 1, 'Belfast': 0.95, 'Surrey': 0.95,
        'Southampton': 0.95, 'Essex': 1, 'Kent': 0.9, 'Oxford': 0.95, 'Cambridge': 0.95,
        'Norwich': 0.85, 'York': 0.85, 'Cornwall': 0.8, 'Devon': 0.8, 'Norfolk': 0.75,
        'Scottish Highlands': 0.7, 'North Wales': 0.75, 'South Wales': 0.85, 'Lake District': 0.7,
        'Isle of Wight': 0.75
    }
    garaging_factor = {
        'Garage': 1, 'Street': 1.15, 'Car Park': 1.3, 'Unsecured': 1.5
    }
    vehicle_factor = {
        'Model 3 RWD (2025)': 1.25, 'Model 3 LR RWD (2025)': 1.3, 'Model 3 LR AWD (2025)': 1.4,
        'Model 3 P (2025)': 1.5, 'Model Y RWD (2025)': 1.25, 'Model Y LR RWD (2025)': 1.3,
        'Model Y LR AWD (2025)': 1.35, 'Model 3 RWD': 1.3, 'Model 3 LR RWD': 1.35,
        'Model 3 LR AWD': 1.4, 'Model 3 P': 1.45, 'Model Y RWD': 1.35, 'Model Y LR RWD': 1.3,
        'Model Y LR AWD': 1.4, 'Model Y P': 1.55
    }
    insurance_group_factor = {
        'Model 3 RWD (2025)': 0.76, 'Model 3 LR RWD (2025)': 0.8, 'Model 3 LR AWD (2025)': 0.86,
        'Model 3 P (2025)': 1, 'Model Y RWD (2025)': 0.78, 'Model Y LR RWD (2025)': 0.82,
        'Model Y LR AWD (2025)': 0.88, 'Model 3 RWD': 1, 'Model 3 LR RWD': 0.88,
        'Model 3 LR AWD': 1.04, 'Model 3 P': 1.04, 'Model Y RWD': 0.96, 'Model Y LR RWD': 0.94,
        'Model Y LR AWD': 1, 'Model Y P': 1.04
    }
    vehicle_use_factor = {
        'Social': 1, 'Social + Commuting': 1.15, 'Social + Commuting + Business': 1.3
    }
    mileage_factor = {
        3000: 0.85, 4000: 0.87, 5000: 0.89, 6000: 0.9, 7000: 0.95, 7500: 1,
        8000: 1.02, 9000: 1.04, 10000: 1.06, 12000: 1.1, 15000: 1.15, 18000: 1.2, 20000: 1.25
    }
    excess_factor = {
        '0-100': 1.1, '101-250': 1, '251-500': 0.95, '501-1000': 0.9, '>1000': 0.85
    }

    # Weightings
    weightings = {
        'age': 0.15, 'driving_experience': 0.10, 'driving_record': 0.15, 'no_claims_discount': 0.20,
        'location': 0.10, 'garaging': 0.05, 'vehicle': 0.10, 'insurance_group': 0.10,
        'vehicle_use': 0.05, 'mileage': 0.05, 'excess': 0.05
    }

    # Extract customer data
    factors = {
        'age': age_factor[customer_data['age']],
        'driving_experience': driving_experience_factor[customer_data['driving_experience']],
        'driving_record': driving_record_factor[customer_data['driving_record']],
        'no_claims_discount': no_claims_discount_factor[customer_data['no_claims_years']],
        'location': location_factor[customer_data['location']],
        'garaging': garaging_factor[customer_data['garaging']],
        'vehicle': vehicle_factor[customer_data['vehicle_model']],
        'insurance_group': insurance_group_factor[customer_data['vehicle_model']],
        'vehicle_use': vehicle_use_factor[customer_data['vehicle_use']],
        'mileage': mileage_factor[customer_data['mileage']],
        'excess': excess_factor[customer_data['excess']]
    }

    # Calculate weighted sum
    weighted_sum = sum(weightings[key] * factors[key] for key in factors)

    # Calculate premium
    premium = base_premium * weighted_sum
    return round(premium, 2)

# Streamlit interface
st.title("Lachie Insurance Testing App")

st.header("Select Insurer")
insurer_options = {
    "Aviva": 1000,
    "Admiral": 2500,
    "Wakam": 2000
}
insurer = st.radio("Insurer", list(insurer_options.keys()), index=0)
base_premium = insurer_options[insurer]

st.header("Enter Customer Details")
with st.form("customer_form"):
    age = st.selectbox("Age", list(range(17, 61)))
    driving_experience = st.selectbox("Driving Experience (Years Licensed)", ["<2", "2-5", "5-10", "10-20", ">20"])
    driving_record = st.selectbox("Driving Record Last 5 Years", [
        "Clean Record", "1 Minor Violation", "2 Minor Violations", "1 Major Violation",
        "1 At-Fault Claim", "2 At-Fault Claims", "1 Minor + 1 At-Fault",
        "1 Major + 1 At-Fault", "Multiple Violations/Claims"
    ])
    no_claims_years = st.slider("No Claims Discount Years", 0, 9, 5)
    location = st.selectbox("Location", [
        "Central London", "Outer London", "Birmingham", "Manchester", "Leeds", "Glasgow",
        "Liverpool", "Newcastle", "Sheffield", "Bristol", "Edinburgh", "Cardiff", "Belfast",
        "Surrey", "Southampton", "Essex", "Kent", "Oxford", "Cambridge", "Norwich", "York",
        "Cornwall", "Devon", "Norfolk", "Scottish Highlands", "North Wales", "South Wales",
        "Lake District", "Isle of Wight"
    ])
    garaging = st.selectbox("Garaging", ["Garage", "Street", "Car Park", "Unsecured"])
    vehicle_model = st.selectbox("Vehicle Model", [
        "Model 3 RWD (2025)", "Model 3 LR RWD (2025)", "Model 3 LR AWD (2025)", "Model 3 P (2025)",
        "Model Y RWD (2025)", "Model Y LR RWD (2025)", "Model Y LR AWD (2025)",
        "Model 3 RWD", "Model 3 LR RWD", "Model 3 LR AWD", "Model 3 P",
        "Model Y RWD", "Model Y LR RWD", "Model Y LR AWD", "Model Y P"
    ])
    vehicle_use = st.selectbox("Vehicle Use", ["Social", "Social + Commuting", "Social + Commuting + Business"])
    mileage = st.selectbox("Annual Mileage", [3000, 4000, 5000, 6000, 7000, 7500, 8000, 9000, 10000, 12000, 15000, 18000, 20000])
    excess = st.selectbox("Voluntary Excess (£)", ["0-100", "101-250", "251-500", "501-1000", ">1000"])
    
    submitted = st.form_submit_button("Calculate Premium")

if submitted:
    customer_data = {
        'age': age,
        'driving_experience': driving_experience,
        'driving_record': driving_record,
        'no_claims_years': no_claims_years,
        'location': location,
        'garaging': garaging,
        'vehicle_model': vehicle_model,
        'vehicle_use': vehicle_use,
        'mileage': mileage,
        'excess': excess
    }
    premium = calculate_premium(base_premium, customer_data)
    st.success(f"Calculated Annual Premium: £{premium}")
