function calculateRiskPriority(probability, impact, detectionDifficulty = 1) {
    
    // JavaScript: Risk Priority Number calculation
    const rpn = probability * impact * detectionDifficulty;
    return Math.min(rpn, 1000);
}

function assessFeatureRisk(featureData) {
    
    // JavaScript: Object to store risk assessment
    const riskAssessment = {
        feature_name: featureData.name,
        business_impact: 0,
        technical_complexity: 0,
        user_impact: 0,
        failure_probability: 0,
        total_risk_score: 0
    };
    
    
    // JavaScript: Calculate business impact score
    const businessFactors = featureData.business_factors || {};
    const revenueImpact = businessFactors.revenue_impact || 1;
    const customerImpact = businessFactors.customer_impact || 1;
    const complianceImpact = businessFactors.compliance_impact || 1;
    
    riskAssessment.business_impact = Math.min((revenueImpact + customerImpact + complianceImpact) / 3, 10);
    
    
    // JavaScript: Calculate technical complexity score
    const technicalFactors = featureData.technical_factors || {};
    const codeComplexity = technicalFactors.code_complexity || 1;
    const integrationPoints = technicalFactors.integration_points || 1;
    const dependencyCount = technicalFactors.dependency_count || 1;
    
    riskAssessment.technical_complexity = Math.min((codeComplexity + integrationPoints + dependencyCount) / 3, 10);
    
    
    // JavaScript: Calculate user impact score
    const userFactors = featureData.user_factors || {};
    const userBaseSize = userFactors.user_base_size || 1;
    const featureCriticality = userFactors.feature_criticality || 1;
    const accessibilityImpact = userFactors.accessibility_impact || 1;
    
    riskAssessment.user_impact = Math.min((userBaseSize + featureCriticality + accessibilityImpact) / 3, 10);
    
    
    // JavaScript: Calculate failure probability
    const historicalData = featureData.historical_data || {};
    const defectDensity = historicalData.defect_density || 1;
    const changeFrequency = historicalData.change_frequency || 1;
    const teamExperience = historicalData.team_experience || 10;
    
    riskAssessment.failure_probability = Math.min((defectDensity + changeFrequency + (10 - teamExperience)) / 3, 10);
    
    
    // JavaScript: Calculate total risk score with weights
    const weights = { business: 0.3, technical: 0.25, user: 0.25, probability: 0.2 };
    
    riskAssessment.total_risk_score = (
        riskAssessment.business_impact * weights.business +
        riskAssessment.technical_complexity * weights.technical +
        riskAssessment.user_impact * weights.user +
        riskAssessment.failure_probability * weights.probability
    );
    
    return riskAssessment;
}

function prioritizeTestAreas(featuresList) {
    
    // JavaScript: Array to store prioritized features
    const prioritizedFeatures = [];
    
    for (const feature of featuresList) {
        
        // Assess risk for each feature
        const riskData = assessFeatureRisk(feature);
        
        
        // JavaScript: Add priority level based on risk score
        if (riskData.total_risk_score >= 8) {
            riskData.priority = 'CRITICAL';
            riskData.test_coverage_target = 95;
        } else if (riskData.total_risk_score >= 6) {
            riskData.priority = 'HIGH';
            riskData.test_coverage_target = 85;
        } else if (riskData.total_risk_score >= 4) {
            riskData.priority = 'MEDIUM';
            riskData.test_coverage_target = 70;
        } else {
            riskData.priority = 'LOW';
            riskData.test_coverage_target = 50;
        }
        
        prioritizedFeatures.push(riskData);
    }
    
    
    // JavaScript: Sort by total risk score (descending)
    return prioritizedFeatures.sort((a, b) => b.total_risk_score - a.total_risk_score);
}

function generateTestStrategy(prioritizedFeatures) {
    
    // JavaScript: Object to store test strategy
    const testStrategy = {
        high_risk_features: [],
        medium_risk_features: [],
        low_risk_features: [],
        recommended_test_types: {},
        resource_allocation: {}
    };
    
    
    // JavaScript: Categorize features by risk level
    for (const feature of prioritizedFeatures) {
        if (['CRITICAL', 'HIGH'].includes(feature.priority)) {
            testStrategy.high_risk_features.push(feature);
        } else if (feature.priority === 'MEDIUM') {
            testStrategy.medium_risk_features.push(feature);
        } else {
            testStrategy.low_risk_features.push(feature);
        }
    }
    
    
    // JavaScript: Generate test type recommendations
    for (const feature of prioritizedFeatures) {
        const testTypes = [];
        
        if (feature.technical_complexity >= 7) {
            testTypes.push('Unit Testing', 'Integration Testing', 'API Testing');
        }
        if (feature.user_impact >= 7) {
            testTypes.push('UI Testing', 'Usability Testing', 'Accessibility Testing');
        }
        if (feature.business_impact >= 7) {
            testTypes.push('End-to-End Testing', 'Performance Testing', 'Security Testing');
        }
        if (feature.failure_probability >= 7) {
            testTypes.push('Regression Testing', 'Stress Testing', 'Chaos Testing');
        }
        
        testStrategy.recommended_test_types[feature.feature_name] = [...new Set(testTypes)];
    }
    
    
    // JavaScript: Calculate resource allocation
    const totalFeatures = prioritizedFeatures.length;
    if (totalFeatures > 0) {
        const highRiskCount = testStrategy.high_risk_features.length;
        const mediumRiskCount = testStrategy.medium_risk_features.length;
        const lowRiskCount = testStrategy.low_risk_features.length;
        
        testStrategy.resource_allocation = {
            high_risk_allocation: `${((highRiskCount / totalFeatures) * 60).toFixed(1)}%`,
            medium_risk_allocation: `${((mediumRiskCount / totalFeatures) * 30).toFixed(1)}%`,
            low_risk_allocation: `${((lowRiskCount / totalFeatures) * 10).toFixed(1)}%`
        };
    }
    
    return testStrategy;
}

// Test the Risk-Based Testing Framework
const features = [
    {
        name: 'Payment Processing',
        business_factors: { revenue_impact: 10, customer_impact: 9, compliance_impact: 10 },
        technical_factors: { code_complexity: 8, integration_points: 9, dependency_count: 7 },
        user_factors: { user_base_size: 10, feature_criticality: 10, accessibility_impact: 8 },
        historical_data: { defect_density: 6, change_frequency: 7, team_experience: 6 }
    },
    {
        name: 'User Profile Management',
        business_factors: { revenue_impact: 5, customer_impact: 7, compliance_impact: 6 },
        technical_factors: { code_complexity: 4, integration_points: 5, dependency_count: 3 },
        user_factors: { user_base_size: 8, feature_criticality: 6, accessibility_impact: 7 },
        historical_data: { defect_density: 3, change_frequency: 4, team_experience: 8 }
    }
];

const prioritizedFeatures = prioritizeTestAreas(features);
const testStrategy = generateTestStrategy(prioritizedFeatures);

console.log("=== RISK-BASED TESTING ANALYSIS ===\n");
console.log("Feature Risk Prioritization:");
prioritizedFeatures.forEach(feature => {
    console.log(`• ${feature.feature_name}: ${feature.priority} (Risk Score: ${feature.total_risk_score.toFixed(2)})`);
});

console.log(`\nResource Allocation:`);
Object.entries(testStrategy.resource_allocation).forEach(([allocation, percentage]) => {
    console.log(`• ${allocation.replace(/_/g, ' ')}: ${percentage}`);
});