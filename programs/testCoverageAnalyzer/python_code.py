def analyze_test_coverage(test_results, requirements, code_metrics=None):
    """
    Comprehensive test coverage analysis for quality assurance
    """
    
    # Python: Dictionary to store coverage analysis results
    coverage_analysis = {
        'functional_coverage': {},
        'requirement_coverage': {},
        'code_coverage': {},
        'risk_coverage': {},
        'coverage_gaps': [],
        'quality_metrics': {},
        'recommendations': []
    }
    
    
    # Python: Analyze functional test coverage
    coverage_analysis['functional_coverage'] = analyze_functional_coverage(test_results)
    
    # Python: Analyze requirement coverage
    coverage_analysis['requirement_coverage'] = analyze_requirement_coverage(test_results, requirements)
    
    # Python: Analyze code coverage if metrics provided
    if code_metrics:
        coverage_analysis['code_coverage'] = analyze_code_coverage(code_metrics)
    
    
    # Python: Identify coverage gaps
    coverage_analysis['coverage_gaps'] = identify_coverage_gaps(coverage_analysis)
    
    # Python: Calculate quality metrics
    coverage_analysis['quality_metrics'] = calculate_quality_metrics(coverage_analysis)
    
    # Python: Generate recommendations
    coverage_analysis['recommendations'] = generate_coverage_recommendations(coverage_analysis)
    
    return coverage_analysis

def analyze_functional_coverage(test_results):
    """Analyze functional test coverage across different test types"""
    
    # Python: Dictionary to store functional coverage data
    functional_coverage = {
        'total_tests': 0,
        'passed_tests': 0,
        'failed_tests': 0,
        'skipped_tests': 0,
        'test_type_distribution': {},
        'feature_coverage': {},
        'pass_rate': 0,
        'coverage_by_priority': {}
    }
    
    
    # Python: Calculate basic test statistics
    functional_coverage['total_tests'] = len(test_results)
    functional_coverage['passed_tests'] = len([t for t in test_results if t['status'] == 'passed'])
    functional_coverage['failed_tests'] = len([t for t in test_results if t['status'] == 'failed'])
    functional_coverage['skipped_tests'] = len([t for t in test_results if t['status'] == 'skipped'])
    
    if functional_coverage['total_tests'] > 0:
        functional_coverage['pass_rate'] = (functional_coverage['passed_tests'] / functional_coverage['total_tests']) * 100
    
    
    # Python: Analyze test type distribution
    test_types = {}
    for test in test_results:
        test_type = test.get('type', 'unknown')
        test_types[test_type] = test_types.get(test_type, 0) + 1
    
    functional_coverage['test_type_distribution'] = test_types
    
    
    # Python: Analyze feature coverage
    features = {}
    for test in test_results:
        feature = test.get('feature', 'unknown')
        if feature not in features:
            features[feature] = {'total': 0, 'passed': 0, 'failed': 0}
        
        features[feature]['total'] += 1
        if test['status'] == 'passed':
            features[feature]['passed'] += 1
        elif test['status'] == 'failed':
            features[feature]['failed'] += 1
    
    
    # Python: Calculate coverage percentage for each feature
    for feature, stats in features.items():
        if stats['total'] > 0:
            stats['coverage_percentage'] = (stats['passed'] / stats['total']) * 100
    
    functional_coverage['feature_coverage'] = features
    
    
    # Python: Analyze coverage by priority
    priorities = {}
    for test in test_results:
        priority = test.get('priority', 'medium')
        if priority not in priorities:
            priorities[priority] = {'total': 0, 'passed': 0}
        
        priorities[priority]['total'] += 1
        if test['status'] == 'passed':
            priorities[priority]['passed'] += 1
    
    
    # Python: Calculate coverage percentage by priority
    for priority, stats in priorities.items():
        if stats['total'] > 0:
            stats['coverage_percentage'] = (stats['passed'] / stats['total']) * 100
    
    functional_coverage['coverage_by_priority'] = priorities
    
    return functional_coverage

def analyze_requirement_coverage(test_results, requirements):
    """Analyze how well tests cover business requirements"""
    
    # Python: Dictionary to store requirement coverage data
    requirement_coverage = {
        'total_requirements': len(requirements),
        'covered_requirements': 0,
        'uncovered_requirements': [],
        'requirement_test_mapping': {},
        'coverage_percentage': 0,
        'critical_requirement_coverage': 0
    }
    
    
    # Python: Create mapping of requirements to tests
    req_mapping = {}
    for req in requirements:
        req_id = req['id']
        req_mapping[req_id] = {
            'requirement': req,
            'tests': [],
            'coverage_status': 'not_covered'
        }
    
    
    # Python: Map tests to requirements
    for test in test_results:
        covered_reqs = test.get('covers_requirements', [])
        for req_id in covered_reqs:
            if req_id in req_mapping:
                req_mapping[req_id]['tests'].append(test)
                if test['status'] == 'passed':
                    req_mapping[req_id]['coverage_status'] = 'covered'
                elif req_mapping[req_id]['coverage_status'] != 'covered':
                    req_mapping[req_id]['coverage_status'] = 'partially_covered'
    
    
    # Python: Calculate coverage statistics
    covered_count = 0
    critical_covered = 0
    critical_total = 0
    
    for req_id, mapping in req_mapping.items():
        req = mapping['requirement']
        
        if mapping['coverage_status'] == 'covered':
            covered_count += 1
        
        if req.get('priority') == 'critical':
            critical_total += 1
            if mapping['coverage_status'] == 'covered':
                critical_covered += 1
        
        if mapping['coverage_status'] == 'not_covered':
            requirement_coverage['uncovered_requirements'].append(req)
    
    requirement_coverage['covered_requirements'] = covered_count
    requirement_coverage['requirement_test_mapping'] = req_mapping
    
    if requirement_coverage['total_requirements'] > 0:
        requirement_coverage['coverage_percentage'] = (covered_count / requirement_coverage['total_requirements']) * 100
    
    if critical_total > 0:
        requirement_coverage['critical_requirement_coverage'] = (critical_covered / critical_total) * 100
    
    return requirement_coverage

def analyze_code_coverage(code_metrics):
    """Analyze code coverage metrics"""
    
    # Python: Dictionary to store code coverage analysis
    code_coverage = {
        'line_coverage': 0,
        'branch_coverage': 0,
        'function_coverage': 0,
        'class_coverage': 0,
        'overall_coverage': 0,
        'coverage_by_module': {},
        'uncovered_areas': []
    }
    
    
    # Python: Extract coverage metrics
    code_coverage['line_coverage'] = code_metrics.get('line_coverage', 0)
    code_coverage['branch_coverage'] = code_metrics.get('branch_coverage', 0)
    code_coverage['function_coverage'] = code_metrics.get('function_coverage', 0)
    code_coverage['class_coverage'] = code_metrics.get('class_coverage', 0)
    
    
    # Python: Calculate overall coverage (weighted average)
    weights = {'line': 0.4, 'branch': 0.3, 'function': 0.2, 'class': 0.1}
    code_coverage['overall_coverage'] = (
        code_coverage['line_coverage'] * weights['line'] +
        code_coverage['branch_coverage'] * weights['branch'] +
        code_coverage['function_coverage'] * weights['function'] +
        code_coverage['class_coverage'] * weights['class']
    )
    
    
    # Python: Analyze coverage by module
    module_coverage = code_metrics.get('module_coverage', {})
    for module, coverage in module_coverage.items():
        code_coverage['coverage_by_module'][module] = coverage
        
        if coverage < 70:  # Threshold for acceptable coverage
            code_coverage['uncovered_areas'].append({
                'type': 'module',
                'name': module,
                'coverage': coverage,
                'severity': 'high' if coverage < 50 else 'medium'
            })
    
    return code_coverage

def identify_coverage_gaps(coverage_analysis):
    """Identify gaps in test coverage"""
    
    # Python: List to store identified coverage gaps
    gaps = []
    
    functional_coverage = coverage_analysis['functional_coverage']
    requirement_coverage = coverage_analysis['requirement_coverage']
    code_coverage = coverage_analysis.get('code_coverage', {})
    
    
    # Python: Check functional coverage gaps
    if functional_coverage['pass_rate'] < 85:
        gaps.append({
            'type': 'Functional Coverage',
            'severity': 'HIGH',
            'description': f"Pass rate is {functional_coverage['pass_rate']:.1f}% (below 85% threshold)",
            'impact': 'Quality risk due to test failures'
        })
    
    
    # Python: Check feature coverage gaps
    for feature, stats in functional_coverage['feature_coverage'].items():
        if stats.get('coverage_percentage', 0) < 70:
            gaps.append({
                'type': 'Feature Coverage',
                'severity': 'MEDIUM',
                'description': f"Feature '{feature}' has {stats.get('coverage_percentage', 0):.1f}% coverage",
                'impact': f'Insufficient testing for {feature} functionality'
            })
    
    
    # Python: Check requirement coverage gaps
    if requirement_coverage['coverage_percentage'] < 90:
        gaps.append({
            'type': 'Requirement Coverage',
            'severity': 'HIGH',
            'description': f"Only {requirement_coverage['coverage_percentage']:.1f}% of requirements are covered",
            'impact': 'Business requirements may not be fully validated'
        })
    
    if requirement_coverage['critical_requirement_coverage'] < 100:
        gaps.append({
            'type': 'Critical Requirement Coverage',
            'severity': 'CRITICAL',
            'description': f"Critical requirements coverage is {requirement_coverage['critical_requirement_coverage']:.1f}%",
            'impact': 'High-priority business functions may be at risk'
        })
    
    
    # Python: Check code coverage gaps
    if code_coverage and code_coverage['overall_coverage'] < 80:
        gaps.append({
            'type': 'Code Coverage',
            'severity': 'MEDIUM',
            'description': f"Overall code coverage is {code_coverage['overall_coverage']:.1f}%",
            'impact': 'Potential untested code paths'
        })
    
    return gaps

def calculate_quality_metrics(coverage_analysis):
    """Calculate overall quality metrics based on coverage analysis"""
    
    # Python: Dictionary to store quality metrics
    quality_metrics = {
        'overall_quality_score': 0,
        'test_effectiveness': 0,
        'coverage_completeness': 0,
        'risk_level': 'UNKNOWN',
        'quality_trend': 'STABLE',
        'confidence_level': 0
    }
    
    functional_coverage = coverage_analysis['functional_coverage']
    requirement_coverage = coverage_analysis['requirement_coverage']
    code_coverage = coverage_analysis.get('code_coverage', {})
    gaps = coverage_analysis['coverage_gaps']
    
    
    # Python: Calculate test effectiveness (based on pass rate and coverage)
    pass_rate = functional_coverage['pass_rate']
    req_coverage = requirement_coverage['coverage_percentage']
    
    quality_metrics['test_effectiveness'] = (pass_rate + req_coverage) / 2
    
    
    # Python: Calculate coverage completeness
    coverage_scores = [req_coverage]
    if code_coverage:
        coverage_scores.append(code_coverage['overall_coverage'])
    
    quality_metrics['coverage_completeness'] = sum(coverage_scores) / len(coverage_scores)
    
    
    # Python: Calculate overall quality score
    weights = {
        'effectiveness': 0.4,
        'completeness': 0.4,
        'gap_penalty': 0.2
    }
    
    gap_penalty = min(len(gaps) * 5, 50)  # Max 50% penalty for gaps
    
    quality_metrics['overall_quality_score'] = (
        quality_metrics['test_effectiveness'] * weights['effectiveness'] +
        quality_metrics['coverage_completeness'] * weights['completeness'] -
        gap_penalty * weights['gap_penalty']
    )
    
    quality_metrics['overall_quality_score'] = max(0, quality_metrics['overall_quality_score'])
    
    
    # Python: Determine risk level
    if quality_metrics['overall_quality_score'] >= 85:
        quality_metrics['risk_level'] = 'LOW'
    elif quality_metrics['overall_quality_score'] >= 70:
        quality_metrics['risk_level'] = 'MEDIUM'
    elif quality_metrics['overall_quality_score'] >= 50:
        quality_metrics['risk_level'] = 'HIGH'
    else:
        quality_metrics['risk_level'] = 'CRITICAL'
    
    
    # Python: Calculate confidence level
    critical_gaps = len([g for g in gaps if g['severity'] in ['HIGH', 'CRITICAL']])
    if critical_gaps == 0 and quality_metrics['overall_quality_score'] >= 80:
        quality_metrics['confidence_level'] = 90
    elif critical_gaps <= 1 and quality_metrics['overall_quality_score'] >= 70:
        quality_metrics['confidence_level'] = 75
    elif critical_gaps <= 2 and quality_metrics['overall_quality_score'] >= 60:
        quality_metrics['confidence_level'] = 60
    else:
        quality_metrics['confidence_level'] = 40
    
    return quality_metrics

def generate_coverage_recommendations(coverage_analysis):
    """Generate recommendations to improve test coverage"""
    
    # Python: List to store recommendations
    recommendations = []
    
    gaps = coverage_analysis['coverage_gaps']
    quality_metrics = coverage_analysis['quality_metrics']
    functional_coverage = coverage_analysis['functional_coverage']
    requirement_coverage = coverage_analysis['requirement_coverage']
    
    
    # Python: Recommendations based on quality score
    if quality_metrics['overall_quality_score'] < 70:
        recommendations.append({
            'category': 'Overall Quality',
            'priority': 'HIGH',
            'recommendation': 'Implement comprehensive test improvement plan',
            'actions': [
                'Increase test coverage for critical features',
                'Address all high-severity coverage gaps',
                'Establish quality gates for releases'
            ],
            'expected_impact': 'Significant quality improvement'
        })
    
    
    # Python: Recommendations for functional coverage
    if functional_coverage['pass_rate'] < 85:
        recommendations.append({
            'category': 'Test Stability',
            'priority': 'HIGH',
            'recommendation': 'Improve test reliability and fix failing tests',
            'actions': [
                'Analyze and fix flaky tests',
                'Improve test data management',
                'Enhance test environment stability'
            ],
            'expected_impact': 'Higher test pass rates and reliability'
        })
    
    
    # Python: Recommendations for requirement coverage
    if requirement_coverage['coverage_percentage'] < 90:
        recommendations.append({
            'category': 'Requirement Coverage',
            'priority': 'HIGH',
            'recommendation': 'Increase requirement test coverage',
            'actions': [
                'Create tests for uncovered requirements',
                'Improve requirement traceability',
                'Implement requirement-based test planning'
            ],
            'expected_impact': 'Better business requirement validation'
        })
    
    
    # Python: Recommendations for critical gaps
    critical_gaps = [g for g in gaps if g['severity'] == 'CRITICAL']
    if critical_gaps:
        recommendations.append({
            'category': 'Critical Issues',
            'priority': 'CRITICAL',
            'recommendation': 'Address critical coverage gaps immediately',
            'actions': [
                f'Fix: {gap["description"]}' for gap in critical_gaps[:3]
            ],
            'expected_impact': 'Reduced critical quality risks'
        })
    
    
    # Python: General improvement recommendations
    if quality_metrics['confidence_level'] < 75:
        recommendations.append({
            'category': 'Test Strategy',
            'priority': 'MEDIUM',
            'recommendation': 'Enhance overall test strategy and processes',
            'actions': [
                'Implement risk-based testing approach',
                'Establish automated regression testing',
                'Create comprehensive test documentation',
                'Implement continuous quality monitoring'
            ],
            'expected_impact': 'Improved test effectiveness and coverage'
        })
    
    return recommendations

# Test the Test Coverage Analyzer
if __name__ == "__main__":
    
    # Sample test results data
    test_results = [
        {'id': 'T001', 'status': 'passed', 'type': 'unit', 'feature': 'login', 'priority': 'high', 'covers_requirements': ['REQ001', 'REQ002']},
        {'id': 'T002', 'status': 'passed', 'type': 'integration', 'feature': 'login', 'priority': 'high', 'covers_requirements': ['REQ001']},
        {'id': 'T003', 'status': 'failed', 'type': 'ui', 'feature': 'dashboard', 'priority': 'medium', 'covers_requirements': ['REQ003']},
        {'id': 'T004', 'status': 'passed', 'type': 'api', 'feature': 'payment', 'priority': 'critical', 'covers_requirements': ['REQ004', 'REQ005']},
        {'id': 'T005', 'status': 'skipped', 'type': 'performance', 'feature': 'payment', 'priority': 'low', 'covers_requirements': ['REQ006']},
        {'id': 'T006', 'status': 'passed', 'type': 'security', 'feature': 'authentication', 'priority': 'critical', 'covers_requirements': ['REQ007']},
        {'id': 'T007', 'status': 'failed', 'type': 'ui', 'feature': 'dashboard', 'priority': 'medium', 'covers_requirements': ['REQ008']},
        {'id': 'T008', 'status': 'passed', 'type': 'unit', 'feature': 'reporting', 'priority': 'low', 'covers_requirements': ['REQ009']}
    ]
    
    # Sample requirements data
    requirements = [
        {'id': 'REQ001', 'description': 'User login functionality', 'priority': 'critical'},
        {'id': 'REQ002', 'description': 'Password validation', 'priority': 'high'},
        {'id': 'REQ003', 'description': 'Dashboard display', 'priority': 'medium'},
        {'id': 'REQ004', 'description': 'Payment processing', 'priority': 'critical'},
        {'id': 'REQ005', 'description': 'Payment validation', 'priority': 'critical'},
        {'id': 'REQ006', 'description': 'Payment performance', 'priority': 'medium'},
        {'id': 'REQ007', 'description': 'Authentication security', 'priority': 'critical'},
        {'id': 'REQ008', 'description': 'Dashboard navigation', 'priority': 'medium'},
        {'id': 'REQ009', 'description': 'Report generation', 'priority': 'low'},
        {'id': 'REQ010', 'description': 'Data export', 'priority': 'medium'}  # Uncovered requirement
    ]
    
    # Sample code coverage metrics
    code_metrics = {
        'line_coverage': 78,
        'branch_coverage': 65,
        'function_coverage': 85,
        'class_coverage': 72,
        'module_coverage': {
            'authentication': 90,
            'payment': 75,
            'dashboard': 60,
            'reporting': 45
        }
    }
    
    
    # Perform coverage analysis
    analysis = analyze_test_coverage(test_results, requirements, code_metrics)
    
    
    # Display results
    print("=== TEST COVERAGE ANALYSIS ===\n")
    
    print("Functional Coverage:")
    fc = analysis['functional_coverage']
    print(f"• Total Tests: {fc['total_tests']}")
    print(f"• Pass Rate: {fc['pass_rate']:.1f}%")
    print(f"• Test Types: {', '.join(fc['test_type_distribution'].keys())}")
    
    print(f"\nRequirement Coverage:")
    rc = analysis['requirement_coverage']
    print(f"• Overall Coverage: {rc['coverage_percentage']:.1f}%")
    print(f"• Critical Requirements: {rc['critical_requirement_coverage']:.1f}%")
    print(f"• Uncovered Requirements: {len(rc['uncovered_requirements'])}")
    
    print(f"\nCode Coverage:")
    cc = analysis['code_coverage']
    print(f"• Overall Coverage: {cc['overall_coverage']:.1f}%")
    print(f"• Line Coverage: {cc['line_coverage']}%")
    print(f"• Branch Coverage: {cc['branch_coverage']}%")
    
    print(f"\nQuality Metrics:")
    qm = analysis['quality_metrics']
    print(f"• Overall Quality Score: {qm['overall_quality_score']:.1f}")
    print(f"• Risk Level: {qm['risk_level']}")
    print(f"• Confidence Level: {qm['confidence_level']}%")
    
    print(f"\nCoverage Gaps ({len(analysis['coverage_gaps'])}):")
    for gap in analysis['coverage_gaps']:
        print(f"• {gap['type']} ({gap['severity']}): {gap['description']}")
    
    print(f"\nRecommendations:")
    for rec in analysis['recommendations']:
        print(f"• {rec['category']} ({rec['priority']}): {rec['recommendation']}")
        if 'actions' in rec:
            for action in rec['actions'][:2]:  # Show first 2 actions
                print(f"  - {action}")
        print()