import time
import statistics
from collections import defaultdict

def analyze_performance_metrics(response_times, throughput_data, resource_usage):
    """
    Analyze performance metrics to identify bottlenecks and optimization opportunities
    """
    
    # Python: Dictionary to store performance analysis results
    analysis_results = {
        'response_time_analysis': {},
        'throughput_analysis': {},
        'resource_analysis': {},
        'bottleneck_indicators': [],
        'recommendations': []
    }
    
    
    # Python: Analyze response time patterns
    analysis_results['response_time_analysis'] = analyze_response_times(response_times)
    
    # Python: Analyze throughput patterns
    analysis_results['throughput_analysis'] = analyze_throughput(throughput_data)
    
    # Python: Analyze resource utilization
    analysis_results['resource_analysis'] = analyze_resource_usage(resource_usage)
    
    
    # Python: Identify bottlenecks based on analysis
    analysis_results['bottleneck_indicators'] = identify_bottlenecks(analysis_results)
    
    # Python: Generate optimization recommendations
    analysis_results['recommendations'] = generate_recommendations(analysis_results)
    
    return analysis_results

def analyze_response_times(response_times):
    """Analyze response time patterns and identify anomalies"""
    
    # Python: Dictionary to store response time analysis
    rt_analysis = {
        'mean_response_time': 0,
        'median_response_time': 0,
        'p95_response_time': 0,
        'p99_response_time': 0,
        'max_response_time': 0,
        'min_response_time': 0,
        'std_deviation': 0,
        'outliers': [],
        'trend': 'stable'
    }
    
    if not response_times:
        return rt_analysis
    
    
    # Python: Calculate basic statistics
    rt_analysis['mean_response_time'] = statistics.mean(response_times)
    rt_analysis['median_response_time'] = statistics.median(response_times)
    rt_analysis['max_response_time'] = max(response_times)
    rt_analysis['min_response_time'] = min(response_times)
    rt_analysis['std_deviation'] = statistics.stdev(response_times) if len(response_times) > 1 else 0
    
    
    # Python: Calculate percentiles
    sorted_times = sorted(response_times)
    rt_analysis['p95_response_time'] = calculate_percentile(sorted_times, 95)
    rt_analysis['p99_response_time'] = calculate_percentile(sorted_times, 99)
    
    
    # Python: Identify outliers using IQR method
    q1 = calculate_percentile(sorted_times, 25)
    q3 = calculate_percentile(sorted_times, 75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    rt_analysis['outliers'] = [t for t in response_times if t < lower_bound or t > upper_bound]
    
    
    # Python: Determine trend (simplified analysis)
    if len(response_times) >= 10:
        first_half_avg = statistics.mean(response_times[:len(response_times)//2])
        second_half_avg = statistics.mean(response_times[len(response_times)//2:])
        
        if second_half_avg > first_half_avg * 1.2:
            rt_analysis['trend'] = 'degrading'
        elif second_half_avg < first_half_avg * 0.8:
            rt_analysis['trend'] = 'improving'
        else:
            rt_analysis['trend'] = 'stable'
    
    return rt_analysis

def analyze_throughput(throughput_data):
    """Analyze throughput patterns and capacity limits"""
    
    # Python: Dictionary to store throughput analysis
    tp_analysis = {
        'average_throughput': 0,
        'peak_throughput': 0,
        'minimum_throughput': 0,
        'throughput_variance': 0,
        'capacity_utilization': 0,
        'saturation_points': [],
        'throughput_trend': 'stable'
    }
    
    if not throughput_data:
        return tp_analysis
    
    
    # Python: Calculate throughput statistics
    tp_analysis['average_throughput'] = statistics.mean(throughput_data)
    tp_analysis['peak_throughput'] = max(throughput_data)
    tp_analysis['minimum_throughput'] = min(throughput_data)
    tp_analysis['throughput_variance'] = statistics.variance(throughput_data) if len(throughput_data) > 1 else 0
    
    
    # Python: Calculate capacity utilization (assuming peak is near capacity)
    if tp_analysis['peak_throughput'] > 0:
        tp_analysis['capacity_utilization'] = (tp_analysis['average_throughput'] / tp_analysis['peak_throughput']) * 100
    
    
    # Python: Identify saturation points (where throughput plateaus despite increased load)
    saturation_threshold = tp_analysis['peak_throughput'] * 0.95
    tp_analysis['saturation_points'] = [i for i, tp in enumerate(throughput_data) 
                                       if tp >= saturation_threshold]
    
    
    # Python: Analyze throughput trend
    if len(throughput_data) >= 10:
        first_quarter = throughput_data[:len(throughput_data)//4]
        last_quarter = throughput_data[-len(throughput_data)//4:]
        
        first_avg = statistics.mean(first_quarter)
        last_avg = statistics.mean(last_quarter)
        
        if last_avg < first_avg * 0.8:
            tp_analysis['throughput_trend'] = 'declining'
        elif last_avg > first_avg * 1.2:
            tp_analysis['throughput_trend'] = 'increasing'
        else:
            tp_analysis['throughput_trend'] = 'stable'
    
    return tp_analysis

def analyze_resource_usage(resource_usage):
    """Analyze CPU, memory, and I/O resource utilization"""
    
    # Python: Dictionary to store resource analysis
    resource_analysis = {
        'cpu_analysis': {},
        'memory_analysis': {},
        'io_analysis': {},
        'resource_bottlenecks': []
    }
    
    
    # Python: Analyze CPU usage
    if 'cpu' in resource_usage:
        cpu_data = resource_usage['cpu']
        resource_analysis['cpu_analysis'] = {
            'average_cpu': statistics.mean(cpu_data),
            'peak_cpu': max(cpu_data),
            'cpu_spikes': len([c for c in cpu_data if c > 80]),
            'cpu_trend': analyze_trend(cpu_data)
        }
        
        if resource_analysis['cpu_analysis']['average_cpu'] > 70:
            resource_analysis['resource_bottlenecks'].append('CPU utilization high')
    
    
    # Python: Analyze memory usage
    if 'memory' in resource_usage:
        memory_data = resource_usage['memory']
        resource_analysis['memory_analysis'] = {
            'average_memory': statistics.mean(memory_data),
            'peak_memory': max(memory_data),
            'memory_growth': analyze_memory_growth(memory_data),
            'memory_trend': analyze_trend(memory_data)
        }
        
        if resource_analysis['memory_analysis']['average_memory'] > 80:
            resource_analysis['resource_bottlenecks'].append('Memory utilization high')
    
    
    # Python: Analyze I/O usage
    if 'io' in resource_usage:
        io_data = resource_usage['io']
        resource_analysis['io_analysis'] = {
            'average_io': statistics.mean(io_data),
            'peak_io': max(io_data),
            'io_wait_time': calculate_io_wait_time(io_data),
            'io_trend': analyze_trend(io_data)
        }
        
        if resource_analysis['io_analysis']['average_io'] > 75:
            resource_analysis['resource_bottlenecks'].append('I/O utilization high')
    
    return resource_analysis

def identify_bottlenecks(analysis_results):
    """Identify performance bottlenecks based on analysis results"""
    
    # Python: List to store identified bottlenecks
    bottlenecks = []
    
    rt_analysis = analysis_results['response_time_analysis']
    tp_analysis = analysis_results['throughput_analysis']
    resource_analysis = analysis_results['resource_analysis']
    
    
    # Python: Check response time bottlenecks
    if rt_analysis.get('p95_response_time', 0) > 2000:  # 2 seconds
        bottlenecks.append({
            'type': 'Response Time',
            'severity': 'HIGH',
            'description': f"95th percentile response time is {rt_analysis['p95_response_time']:.0f}ms",
            'impact': 'User experience degradation'
        })
    
    if rt_analysis.get('trend') == 'degrading':
        bottlenecks.append({
            'type': 'Response Time Trend',
            'severity': 'MEDIUM',
            'description': 'Response times are degrading over time',
            'impact': 'Progressive performance deterioration'
        })
    
    
    # Python: Check throughput bottlenecks
    if tp_analysis.get('capacity_utilization', 0) > 85:
        bottlenecks.append({
            'type': 'Throughput Capacity',
            'severity': 'HIGH',
            'description': f"System operating at {tp_analysis['capacity_utilization']:.1f}% capacity",
            'impact': 'Limited scalability headroom'
        })
    
    if len(tp_analysis.get('saturation_points', [])) > 5:
        bottlenecks.append({
            'type': 'Throughput Saturation',
            'severity': 'MEDIUM',
            'description': 'Multiple saturation points detected',
            'impact': 'System reaching capacity limits'
        })
    
    
    # Python: Check resource bottlenecks
    for bottleneck in resource_analysis.get('resource_bottlenecks', []):
        bottlenecks.append({
            'type': 'Resource Utilization',
            'severity': 'HIGH',
            'description': bottleneck,
            'impact': 'System resource constraints'
        })
    
    return bottlenecks

def generate_recommendations(analysis_results):
    """Generate optimization recommendations based on bottleneck analysis"""
    
    # Python: List to store recommendations
    recommendations = []
    
    bottlenecks = analysis_results['bottleneck_indicators']
    rt_analysis = analysis_results['response_time_analysis']
    tp_analysis = analysis_results['throughput_analysis']
    
    
    # Python: Response time optimization recommendations
    if rt_analysis.get('p95_response_time', 0) > 2000:
        recommendations.append({
            'category': 'Performance Optimization',
            'priority': 'HIGH',
            'recommendation': 'Implement caching strategy to reduce response times',
            'expected_impact': '30-50% response time improvement',
            'implementation_effort': 'Medium'
        })
        
        recommendations.append({
            'category': 'Database Optimization',
            'priority': 'HIGH',
            'recommendation': 'Optimize database queries and add appropriate indexes',
            'expected_impact': '20-40% response time improvement',
            'implementation_effort': 'Medium'
        })
    
    
    # Python: Throughput optimization recommendations
    if tp_analysis.get('capacity_utilization', 0) > 85:
        recommendations.append({
            'category': 'Scalability',
            'priority': 'HIGH',
            'recommendation': 'Implement horizontal scaling or load balancing',
            'expected_impact': '2x-5x throughput increase',
            'implementation_effort': 'High'
        })
        
        recommendations.append({
            'category': 'Resource Management',
            'priority': 'MEDIUM',
            'recommendation': 'Implement connection pooling and resource optimization',
            'expected_impact': '15-25% throughput improvement',
            'implementation_effort': 'Low'
        })
    
    
    # Python: General optimization recommendations
    if len(bottlenecks) > 3:
        recommendations.append({
            'category': 'Monitoring',
            'priority': 'HIGH',
            'recommendation': 'Implement comprehensive performance monitoring and alerting',
            'expected_impact': 'Proactive issue detection and resolution',
            'implementation_effort': 'Medium'
        })
        
        recommendations.append({
            'category': 'Testing Strategy',
            'priority': 'MEDIUM',
            'recommendation': 'Establish regular performance testing and benchmarking',
            'expected_impact': 'Prevent performance regressions',
            'implementation_effort': 'Medium'
        })
    
    return recommendations

def calculate_percentile(sorted_data, percentile):
    """Calculate percentile value from sorted data"""
    if not sorted_data:
        return 0
    
    # Python: Calculate percentile index
    index = (percentile / 100) * (len(sorted_data) - 1)
    
    if index.is_integer():
        return sorted_data[int(index)]
    else:
        
        # Python: Interpolate between values
        lower_index = int(index)
        upper_index = lower_index + 1
        
        if upper_index >= len(sorted_data):
            return sorted_data[-1]
        
        weight = index - lower_index
        return sorted_data[lower_index] * (1 - weight) + sorted_data[upper_index] * weight

def analyze_trend(data):
    """Analyze trend in time series data"""
    if len(data) < 5:
        return 'insufficient_data'
    
    # Python: Simple trend analysis using first and last quarters
    first_quarter = data[:len(data)//4]
    last_quarter = data[-len(data)//4:]
    
    first_avg = statistics.mean(first_quarter)
    last_avg = statistics.mean(last_quarter)
    
    if last_avg > first_avg * 1.1:
        return 'increasing'
    elif last_avg < first_avg * 0.9:
        return 'decreasing'
    else:
        return 'stable'

def analyze_memory_growth(memory_data):
    """Analyze memory growth patterns to detect leaks"""
    if len(memory_data) < 10:
        return 'insufficient_data'
    
    # Python: Check for consistent memory growth (potential leak)
    growth_points = 0
    for i in range(1, len(memory_data)):
        if memory_data[i] > memory_data[i-1]:
            growth_points += 1
    
    growth_ratio = growth_points / (len(memory_data) - 1)
    
    if growth_ratio > 0.7:
        return 'potential_leak'
    elif growth_ratio > 0.4:
        return 'moderate_growth'
    else:
        return 'stable'

def calculate_io_wait_time(io_data):
    """Calculate average I/O wait time"""
    if not io_data:
        return 0
    
    # Python: Simplified I/O wait calculation
    high_io_points = [io for io in io_data if io > 50]
    
    if high_io_points:
        return statistics.mean(high_io_points)
    else:
        return statistics.mean(io_data)

# Test the Performance Bottleneck Detector
if __name__ == "__main__":
    
    # Sample performance data
    response_times = [120, 150, 180, 200, 250, 300, 450, 600, 800, 1200, 
                     1500, 2000, 2500, 1800, 1600, 1400, 1200, 1000, 900, 800]
    
    throughput_data = [100, 120, 140, 160, 180, 190, 195, 198, 199, 200,
                      200, 199, 198, 195, 190, 185, 180, 175, 170, 165]
    
    resource_usage = {
        'cpu': [45, 50, 55, 60, 70, 75, 80, 85, 90, 95, 
               88, 85, 82, 78, 75, 72, 70, 68, 65, 62],
        'memory': [60, 62, 64, 66, 68, 70, 72, 74, 76, 78,
                  80, 82, 84, 86, 88, 90, 92, 94, 96, 98],
        'io': [30, 35, 40, 45, 50, 55, 60, 70, 80, 85,
              82, 78, 75, 72, 68, 65, 62, 58, 55, 52]
    }
    
    
    # Perform performance analysis
    analysis = analyze_performance_metrics(response_times, throughput_data, resource_usage)
    
    
    # Display results
    print("=== PERFORMANCE BOTTLENECK ANALYSIS ===\n")
    
    print("Response Time Analysis:")
    rt = analysis['response_time_analysis']
    print(f"• Mean Response Time: {rt['mean_response_time']:.0f}ms")
    print(f"• 95th Percentile: {rt['p95_response_time']:.0f}ms")
    print(f"• 99th Percentile: {rt['p99_response_time']:.0f}ms")
    print(f"• Trend: {rt['trend']}")
    print(f"• Outliers Detected: {len(rt['outliers'])}")
    
    print(f"\nThroughput Analysis:")
    tp = analysis['throughput_analysis']
    print(f"• Average Throughput: {tp['average_throughput']:.1f} req/s")
    print(f"• Peak Throughput: {tp['peak_throughput']:.1f} req/s")
    print(f"• Capacity Utilization: {tp['capacity_utilization']:.1f}%")
    print(f"• Trend: {tp['throughput_trend']}")
    
    print(f"\nBottlenecks Identified:")
    for bottleneck in analysis['bottleneck_indicators']:
        print(f"• {bottleneck['type']} ({bottleneck['severity']}): {bottleneck['description']}")
    
    print(f"\nRecommendations:")
    for rec in analysis['recommendations']:
        print(f"• {rec['category']} ({rec['priority']}): {rec['recommendation']}")
        print(f"  Expected Impact: {rec['expected_impact']}")
        print(f"  Implementation Effort: {rec['implementation_effort']}\n")