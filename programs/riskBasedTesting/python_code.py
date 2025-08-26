def calculate_risk_priority(probability, impact, detection_difficulty=1):
    """
    Calculate Risk Priority Number (RPN) for test planning
    RPN = Probability × Impact × Detection Difficulty
    """
    
    # Python: Risk Priority Number calculation
    rpn = probability * impact * detection_difficulty
    
    return min(rpn, 1000)  # Cap at 1000 for standardization

def assess_feature_risk(feature_data):
    """Assess risk level for individual features"""
    
    # Python: Dictionary to store risk assessment
    risk_assessment = {
        'feature_name': feature_data['name'],
        'business_impact': 0,
        'technical_complexity': 0,
        'user_impact': 0,
        'failure_probability': 0,
        'total_risk_score': 0
    }
    
    
    # Python: Calculate business impact score (1-10)
    business_factors = feature_data.get('business_factors', {})
    revenue_impact = business_factors.get('revenue_impact', 1)
    customer_impact = business_factors.get('customer_impact', 1)
    compliance_impact = business_factors.get('compliance_impact', 1)
    
    risk_assessment['business_impact'] = min(
        (revenue_impact + customer_impact + compliance_impact) / 3, 10
    )
    
    
    # Python: Calculate technical complexity score (1-10)
    technical_factors = feature_data.get('technical_factors', {})
    code_complexity = technical_factors.get('code_complexity', 1)
    integration_points = technical_factors.get('integration_points', 1)
    dependency_count = technical_factors.get('dependency_count', 1)
    
    risk_assessment['technical_complexity'] = min(
        (code_complexity + integration_points + dependency_count) / 3, 10
    )
    
    
    # Python: Calculate user impact score (1-10)
    user_factors = feature_data.get('user_factors', {})
    user_base_size = user_factors.get('user_base_size', 1)
    feature_criticality = user_factors.get('feature_criticality', 1)
    accessibility_impact = user_factors.get('accessibility_impact', 1)
    
    risk_assessment['user_impact'] = min(
        (user_base_size + feature_criticality + accessibility_impact) / 3, 10
    )
    
    
    # Python: Calculate failure probability based on historical data
    historical_data = feature_data.get('historical_data', {})
    defect_density = historical_data.get('defect_density', 1)
    change_frequency = historical_data.get('change_frequency', 1)
    team_experience = historical_data.get('team_experience', 10)  # Higher is better
    
    risk_assessment['failure_probability'] = min(
        (defect_density + change_frequency + (10 - team_experience)) / 3, 10
    )
    
    
    # Python: Calculate total risk score
    weights = {
        'business': 0.3,
        'technical': 0.25,
        'user': 0.25,
        'probability': 0.2
    }
    
    risk_assessment['total_risk_score'] = (
        risk_assessment['business_impact'] * weights['business'] +
        risk_assessment['technical_complexity'] * weights['technical'] +
        risk_assessment['user_impact'] * weights['user'] +
        risk_assessment['failure_probability'] * weights['probability']
    )
    
    return risk_assessment

def prioritize_test_areas(features_list):
    """Prioritize testing areas based on risk assessment"""
    
    # Python: List to store prioritized features
    prioritized_features = []
    
    for feature in features_list:
        
        # Assess risk for each feature
        risk_data = assess_feature_risk(feature)
        
        # Add priority level based on risk score
        if risk_data['total_risk_score'] >= 8:
            risk_data['priority'] = 'CRITICAL'
            risk_data['test_coverage_target'] = 95
        elif risk_data['total_risk_score'] >= 6:
            risk_data['priority'] = 'HIGH'
            risk_data['test_coverage_target'] = 85
        elif risk_data['total_risk_score'] >= 4:
            risk_data['priority'] = 'MEDIUM'
            risk_data['test_coverage_target'] = 70
        else:
            risk_data['priority'] = 'LOW'
            risk_data['test_coverage_target'] = 50
        
        prioritized_features.append(risk_data)
    
    
    # Python: Sort by total risk score (descending)
    prioritized_features.sort(key=lambda x: x['total_risk_score'], reverse=True)
    
    return prioritized_features

def generate_test_strategy(prioritized_features):
    """Generate comprehensive test strategy based on risk analysis"""
    
    # Python: Dictionary to store test strategy
    test_strategy = {
        'high_risk_features': [],
        'medium_risk_features': [],
        'low_risk_features': [],
        'recommended_test_types': {},
        'resource_allocation': {},
        'timeline_recommendations': {}
    }
    
    
    # Python: Categorize features by risk level
    for feature in prioritized_features:
        if feature['priority'] in ['CRITICAL', 'HIGH']:
            test_strategy['high_risk_features'].append(feature)
        elif feature['priority'] == 'MEDIUM':
            test_strategy['medium_risk_features'].append(feature)
        else:
            test_strategy['low_risk_features'].append(feature)
    
    
    # Python: Generate test type recommendations
    for feature in prioritized_features:
        feature_name = feature['feature_name']
        test_types = []
        
        if feature['technical_complexity'] >= 7:
            test_types.extend(['Unit Testing', 'Integration Testing', 'API Testing'])
        
        if feature['user_impact'] >= 7:
            test_types.extend(['UI Testing', 'Usability Testing', 'Accessibility Testing'])
        
        if feature['business_impact'] >= 7:
            test_types.extend(['End-to-End Testing', 'Performance Testing', 'Security Testing'])
        
        if feature['failure_probability'] >= 7:
            test_types.extend(['Regression Testing', 'Stress Testing', 'Chaos Testing'])
        
        test_strategy['recommended_test_types'][feature_name] = list(set(test_types))
    
    
    # Python: Calculate resource allocation recommendations
    total_features = len(prioritized_features)
    if total_features > 0:
        high_risk_count = len(test_strategy['high_risk_features'])
        medium_risk_count = len(test_strategy['medium_risk_features'])
        low_risk_count = len(test_strategy['low_risk_features'])
        
        test_strategy['resource_allocation'] = {
            'high_risk_allocation': f"{(high_risk_count / total_features) * 60:.1f}%",
            'medium_risk_allocation': f"{(medium_risk_count / total_features) * 30:.1f}%",
            'low_risk_allocation': f"{(low_risk_count / total_features) * 10:.1f}%"
        }
    
    return test_strategy

def generate_risk_report(test_strategy):
    """Generate comprehensive risk-based testing report"""
    
    # Python: Create detailed risk report
    report = {
        'executive_summary': {},
        'risk_distribution': {},
        'testing_recommendations': {},
        'mitigation_strategies': []
    }
    
    
    # Python: Executive summary
    total_features = (len(test_strategy['high_risk_features']) + 
                     len(test_strategy['medium_risk_features']) + 
                     len(test_strategy['low_risk_features']))
    
    report['executive_summary'] = {
        'total_features_analyzed': total_features,
        'high_risk_features': len(test_strategy['high_risk_features']),
        'critical_areas_identified': len([f for f in test_strategy['high_risk_features'] 
                                        if f['priority'] == 'CRITICAL']),
        'recommended_focus_areas': [f['feature_name'] for f in test_strategy['high_risk_features'][:3]]
    }
    
    
    # Python: Risk distribution analysis
    if total_features > 0:
        report['risk_distribution'] = {
            'high_risk_percentage': f"{(len(test_strategy['high_risk_features']) / total_features) * 100:.1f}%",
            'medium_risk_percentage': f"{(len(test_strategy['medium_risk_features']) / total_features) * 100:.1f}%",
            'low_risk_percentage': f"{(len(test_strategy['low_risk_features']) / total_features) * 100:.1f}%"
        }
    
    
    # Python: Testing recommendations
    report['testing_recommendations'] = {
        'immediate_action_required': [f['feature_name'] for f in test_strategy['high_risk_features']],
        'resource_allocation': test_strategy['resource_allocation'],
        'test_coverage_targets': {f['feature_name']: f['test_coverage_target'] 
                                for f in test_strategy['high_risk_features']}
    }
    
    
    # Python: Mitigation strategies
    report['mitigation_strategies'] = [
        "Implement automated testing for high-risk features",
        "Increase code review coverage for complex components", 
        "Establish monitoring and alerting for critical user paths",
        "Create rollback procedures for high-impact features",
        "Implement feature flags for gradual rollouts"
    ]
    
    return report

# Test the Risk-Based Testing Framework
if __name__ == "__main__":
    
    # Sample feature data for risk assessment
    features = [
        {
            'name': 'Payment Processing',
            'business_factors': {'revenue_impact': 10, 'customer_impact': 9, 'compliance_impact': 10},
            'technical_factors': {'code_complexity': 8, 'integration_points': 9, 'dependency_count': 7},
            'user_factors': {'user_base_size': 10, 'feature_criticality': 10, 'accessibility_impact': 8},
            'historical_data': {'defect_density': 6, 'change_frequency': 7, 'team_experience': 6}
        },
        {
            'name': 'User Profile Management',
            'business_factors': {'revenue_impact': 5, 'customer_impact': 7, 'compliance_impact': 6},
            'technical_factors': {'code_complexity': 4, 'integration_points': 5, 'dependency_count': 3},
            'user_factors': {'user_base_size': 8, 'feature_criticality': 6, 'accessibility_impact': 7},
            'historical_data': {'defect_density': 3, 'change_frequency': 4, 'team_experience': 8}
        },
        {
            'name': 'Notification System',
            'business_factors': {'revenue_impact': 3, 'customer_impact': 5, 'compliance_impact': 2},
            'technical_factors': {'code_complexity': 6, 'integration_points': 7, 'dependency_count': 8},
            'user_factors': {'user_base_size': 9, 'feature_criticality': 4, 'accessibility_impact': 5},
            'historical_data': {'defect_density': 5, 'change_frequency': 6, 'team_experience': 7}
        }
    ]
    
    
    # Perform risk-based testing analysis
    prioritized_features = prioritize_test_areas(features)
    test_strategy = generate_test_strategy(prioritized_features)
    risk_report = generate_risk_report(test_strategy)
    
    
    # Display results
    print("=== RISK-BASED TESTING ANALYSIS ===\n")
    
    print("Feature Risk Prioritization:")
    for feature in prioritized_features:
        print(f"• {feature['feature_name']}: {feature['priority']} "
              f"(Risk Score: {feature['total_risk_score']:.2f})")
    
    print(f"\nExecutive Summary:")
    print(f"• Total Features: {risk_report['executive_summary']['total_features_analyzed']}")
    print(f"• High Risk Features: {risk_report['executive_summary']['high_risk_features']}")
    print(f"• Critical Areas: {risk_report['executive_summary']['critical_areas_identified']}")
    
    print(f"\nRecommended Focus Areas:")
    for area in risk_report['executive_summary']['recommended_focus_areas']:
        print(f"• {area}")
    
    print(f"\nResource Allocation:")
    for allocation, percentage in test_strategy['resource_allocation'].items():
        print(f"• {allocation.replace('_', ' ').title()}: {percentage}")