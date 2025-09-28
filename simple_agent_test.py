#!/usr/bin/env python3
"""
SIMPLE COMPREHENSIVE AGENT TESTING
Test all agents including new specialized and super agents
"""

import asyncio
import logging
from typing import Dict, Any
from datetime import datetime

# Import agent testing components
from register_new_agents import NewAgentRegistrar

class SimpleAgentTester:
    """Simple comprehensive testing system for all agents"""
    
    def __init__(self):
        self.registrar = NewAgentRegistrar()
        self.test_results = {
            'specialized_agents': {},
            'super_agents': {},
            'system_integration': {},
            'overall_status': 'pending'
        }
    
    async def run_comprehensive_tests(self):
        """Run comprehensive tests on all agents"""
        logging.info("🧪 Starting simple comprehensive agent testing...")
        
        try:
            # Initialize system
            await self.registrar.initialize_system()
            await self.registrar.register_new_specialized_agents()
            await self.registrar.register_new_super_agents()
            
            # Test new agents
            new_agent_tests = await self.registrar.test_new_agents()
            self.test_results['system_integration'] = new_agent_tests
            
            # Test individual new specialized agents
            await self._test_new_specialized_agents()
            
            # Test individual new super agents
            await self._test_new_super_agents()
            
            # Generate comprehensive report
            report = await self._generate_comprehensive_report()
            
            logging.info("✅ Simple comprehensive agent testing completed successfully!")
            return report
            
        except Exception as e:
            logging.error(f"❌ Comprehensive testing failed: {e}")
            return {
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }
    
    async def _test_new_specialized_agents(self):
        """Test individual new specialized agents"""
        logging.info("🔍 Testing new specialized agents...")
        
        # Test Social Media Agent
        try:
            social_media_result = await self.registrar.new_specialized_agents['social_media_agent'].create_content_calendar({
                'platform': 'all',
                'duration': 14,
                'theme': 'business_growth'
            })
            self.test_results['specialized_agents']['social_media_agent'] = {
                'status': 'success',
                'result': social_media_result.get('status', 'unknown'),
                'capabilities_tested': ['content_calendar_creation', 'hashtag_generation', 'posting_schedule']
            }
        except Exception as e:
            self.test_results['specialized_agents']['social_media_agent'] = {
                'status': 'error',
                'error': str(e)
            }
        
        # Test E-Commerce Agent
        try:
            ecommerce_result = await self.registrar.new_specialized_agents['ecommerce_agent'].optimize_product_listings({
                'products': [
                    {'title': 'Premium Insurance Guide', 'description': 'Comprehensive insurance planning guide', 'price': 25},
                    {'title': 'Music Production Beats', 'description': 'Professional music beats for licensing', 'price': 50}
                ],
                'platform': 'shopify'
            })
            self.test_results['specialized_agents']['ecommerce_agent'] = {
                'status': 'success',
                'result': ecommerce_result.get('status', 'unknown'),
                'capabilities_tested': ['product_optimization', 'seo_improvements', 'pricing_suggestions']
            }
        except Exception as e:
            self.test_results['specialized_agents']['ecommerce_agent'] = {
                'status': 'error',
                'error': str(e)
            }
        
        # Test Customer Service Agent
        try:
            customer_service_result = await self.registrar.new_specialized_agents['customer_service_agent'].handle_customer_inquiry({
                'inquiry': 'I need help with my insurance policy and want to know about pricing options',
                'customer_info': {'name': 'John Doe', 'email': 'john@example.com'},
                'channel': 'email'
            })
            self.test_results['specialized_agents']['customer_service_agent'] = {
                'status': 'success',
                'result': customer_service_result.get('status', 'unknown'),
                'capabilities_tested': ['sentiment_analysis', 'intent_classification', 'response_generation']
            }
        except Exception as e:
            self.test_results['specialized_agents']['customer_service_agent'] = {
                'status': 'error',
                'error': str(e)
            }
        
        # Test Analytics Agent
        try:
            analytics_result = await self.registrar.new_specialized_agents['analytics_agent'].analyze_business_metrics({
                'data': {
                    'conversion': 0.035,
                    'engagement': 0.18,
                    'revenue': 75000,
                    'traffic': 15000,
                    'customer_satisfaction': 4.7
                },
                'metrics': ['conversion', 'engagement', 'revenue', 'traffic', 'customer_satisfaction'],
                'timeframe': '30_days'
            })
            self.test_results['specialized_agents']['analytics_agent'] = {
                'status': 'success',
                'result': analytics_result.get('status', 'unknown'),
                'capabilities_tested': ['metrics_analysis', 'insights_generation', 'recommendations']
            }
        except Exception as e:
            self.test_results['specialized_agents']['analytics_agent'] = {
                'status': 'error',
                'error': str(e)
            }
        
        # Test Automation Agent
        try:
            automation_result = await self.registrar.new_specialized_agents['automation_agent'].create_automation_workflow({
                'workflow_type': 'email_marketing',
                'triggers': ['time_based', 'event_based'],
                'actions': ['email', 'social_media', 'analytics']
            })
            self.test_results['specialized_agents']['automation_agent'] = {
                'status': 'success',
                'result': automation_result.get('status', 'unknown'),
                'capabilities_tested': ['workflow_creation', 'trigger_definition', 'action_setup']
            }
        except Exception as e:
            self.test_results['specialized_agents']['automation_agent'] = {
                'status': 'error',
                'error': str(e)
            }
    
    async def _test_new_super_agents(self):
        """Test individual new super agents"""
        logging.info("🔍 Testing new super agents...")
        
        # Test Digital Marketing Super Agent
        try:
            digital_marketing_result = await self.registrar.new_super_agents['digital_marketing_super_agent'].orchestrate_digital_marketing({
                'campaign_type': 'brand_awareness',
                'budget': 5000,
                'duration': 30,
                'platforms': ['facebook', 'instagram', 'twitter', 'linkedin']
            })
            self.test_results['super_agents']['digital_marketing_super_agent'] = {
                'status': 'success',
                'result': digital_marketing_result.get('status', 'unknown'),
                'capabilities_tested': ['campaign_orchestration', 'content_strategy', 'analytics_integration']
            }
        except Exception as e:
            self.test_results['super_agents']['digital_marketing_super_agent'] = {
                'status': 'error',
                'error': str(e)
            }
        
        # Test E-Commerce Super Agent
        try:
            ecommerce_super_result = await self.registrar.new_super_agents['ecommerce_super_agent'].orchestrate_ecommerce_operations({
                'operation_type': 'product_optimization',
                'products': [
                    {'title': 'Insurance Guide', 'description': 'Comprehensive guide', 'price': 25},
                    {'title': 'Music Beats', 'description': 'Professional beats', 'price': 50}
                ],
                'platform': 'shopify'
            })
            self.test_results['super_agents']['ecommerce_super_agent'] = {
                'status': 'success',
                'result': ecommerce_super_result.get('status', 'unknown'),
                'capabilities_tested': ['operation_orchestration', 'product_optimization', 'analytics_integration']
            }
        except Exception as e:
            self.test_results['super_agents']['ecommerce_super_agent'] = {
                'status': 'error',
                'error': str(e)
            }
        
        # Test Customer Experience Super Agent
        try:
            customer_experience_result = await self.registrar.new_super_agents['customer_experience_super_agent'].orchestrate_customer_experience({
                'customer_data': {
                    'inquiry': 'I need help with my account and billing questions',
                    'satisfaction_score': 4.2,
                    'response_time': 1.5,
                    'total_customers': 1000
                },
                'support_channels': ['email', 'chat', 'phone'],
                'experience_goals': {'satisfaction_target': 4.8, 'response_time_target': 1.0}
            })
            self.test_results['super_agents']['customer_experience_super_agent'] = {
                'status': 'success',
                'result': customer_experience_result.get('status', 'unknown'),
                'capabilities_tested': ['experience_orchestration', 'support_analysis', 'satisfaction_optimization']
            }
        except Exception as e:
            self.test_results['super_agents']['customer_experience_super_agent'] = {
                'status': 'error',
                'error': str(e)
            }
        
        # Test Business Intelligence Super Agent
        try:
            business_intelligence_result = await self.registrar.new_super_agents['business_intelligence_super_agent'].orchestrate_business_intelligence({
                'data_sources': ['sales_data', 'customer_data', 'marketing_data'],
                'analysis_type': 'comprehensive',
                'business_goals': {
                    'revenue': 100000,
                    'conversion_rate': 0.04,
                    'engagement_rate': 0.20,
                    'website_traffic': 20000,
                    'satisfaction_score': 4.8
                }
            })
            self.test_results['super_agents']['business_intelligence_super_agent'] = {
                'status': 'success',
                'result': business_intelligence_result.get('status', 'unknown'),
                'capabilities_tested': ['intelligence_orchestration', 'metrics_analysis', 'predictive_insights']
            }
        except Exception as e:
            self.test_results['super_agents']['business_intelligence_super_agent'] = {
                'status': 'error',
                'error': str(e)
            }
        
        # Test Process Optimization Super Agent
        try:
            process_optimization_result = await self.registrar.new_super_agents['process_optimization_super_agent'].orchestrate_process_optimization({
                'processes': [
                    {'type': 'customer_onboarding', 'triggers': ['new_signup'], 'actions': ['email', 'data_processing']},
                    {'type': 'order_fulfillment', 'triggers': ['payment_completed'], 'actions': ['inventory_update', 'shipping']}
                ],
                'optimization_goals': {
                    'efficiency_target': 0.90,
                    'automation_target': 0.80,
                    'error_threshold': 0.02,
                    'time_target': 1.5,
                    'cost_target': 0.25
                },
                'automation_level': 'high'
            })
            self.test_results['super_agents']['process_optimization_super_agent'] = {
                'status': 'success',
                'result': process_optimization_result.get('status', 'unknown'),
                'capabilities_tested': ['optimization_orchestration', 'workflow_creation', 'efficiency_analysis']
            }
        except Exception as e:
            self.test_results['super_agents']['process_optimization_super_agent'] = {
                'status': 'error',
                'error': str(e)
            }
    
    async def _generate_comprehensive_report(self):
        """Generate comprehensive test report"""
        # Calculate success rates
        specialized_success = sum(1 for agent in self.test_results['specialized_agents'].values() if agent.get('status') == 'success')
        super_agent_success = sum(1 for agent in self.test_results['super_agents'].values() if agent.get('status') == 'success')
        
        total_specialized = len(self.test_results['specialized_agents'])
        total_super = len(self.test_results['super_agents'])
        
        specialized_success_rate = (specialized_success / total_specialized * 100) if total_specialized > 0 else 0
        super_agent_success_rate = (super_agent_success / total_super * 100) if total_super > 0 else 0
        
        # Determine overall status
        if specialized_success_rate == 100 and super_agent_success_rate == 100:
            overall_status = 'excellent'
        elif specialized_success_rate >= 80 and super_agent_success_rate >= 80:
            overall_status = 'good'
        elif specialized_success_rate >= 60 and super_agent_success_rate >= 60:
            overall_status = 'fair'
        else:
            overall_status = 'needs_improvement'
        
        self.test_results['overall_status'] = overall_status
        
        report = {
            'test_summary': {
                'timestamp': datetime.now().isoformat(),
                'overall_status': overall_status,
                'total_agents_tested': total_specialized + total_super,
                'success_rate': f"{((specialized_success + super_agent_success) / (total_specialized + total_super) * 100):.1f}%"
            },
            'specialized_agents': {
                'total': total_specialized,
                'successful': specialized_success,
                'success_rate': f"{specialized_success_rate:.1f}%",
                'details': self.test_results['specialized_agents']
            },
            'super_agents': {
                'total': total_super,
                'successful': super_agent_success,
                'success_rate': f"{super_agent_success_rate:.1f}%",
                'details': self.test_results['super_agents']
            },
            'system_integration': self.test_results['system_integration'],
            'recommendations': self._generate_recommendations()
        }
        
        return report
    
    def _generate_recommendations(self):
        """Generate recommendations based on test results"""
        recommendations = []
        
        # Check for failed agents
        failed_specialized = [name for name, result in self.test_results['specialized_agents'].items() if result.get('status') != 'success']
        failed_super = [name for name, result in self.test_results['super_agents'].items() if result.get('status') != 'success']
        
        if failed_specialized:
            recommendations.append(f"Review and fix failed specialized agents: {', '.join(failed_specialized)}")
        
        if failed_super:
            recommendations.append(f"Review and fix failed super agents: {', '.join(failed_super)}")
        
        # General recommendations
        recommendations.extend([
            "Monitor agent performance regularly",
            "Implement automated health checks",
            "Set up alerting for agent failures",
            "Consider load balancing for high-traffic agents",
            "Document agent capabilities and usage patterns"
        ])
        
        return recommendations

async def main():
    """Main testing function"""
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    
    logger.info("🚀 Starting simple comprehensive agent testing...")
    
    tester = SimpleAgentTester()
    report = await tester.run_comprehensive_tests()
    
    logger.info(f"📊 Test Results: {report.get('test_summary', {}).get('overall_status', 'unknown')}")
    logger.info(f"📈 Success Rate: {report.get('test_summary', {}).get('success_rate', 'unknown')}")
    
    # Print detailed results
    print("\n" + "="*60)
    print("COMPREHENSIVE AGENT TESTING REPORT")
    print("="*60)
    print(f"Overall Status: {report.get('test_summary', {}).get('overall_status', 'unknown').upper()}")
    print(f"Success Rate: {report.get('test_summary', {}).get('success_rate', 'unknown')}")
    print(f"Total Agents Tested: {report.get('test_summary', {}).get('total_agents_tested', 0)}")
    
    print(f"\nSpecialized Agents: {report.get('specialized_agents', {}).get('success_rate', 'unknown')} success rate")
    print(f"Super Agents: {report.get('super_agents', {}).get('success_rate', 'unknown')} success rate")
    
    print("\nRecommendations:")
    for rec in report.get('recommendations', []):
        print(f"• {rec}")
    
    print("\n" + "="*60)

if __name__ == "__main__":
    asyncio.run(main())
