#!/usr/bin/env python3
"""
REGISTER NEW AGENTS
Integration system for registering new specialized and super agents
"""

import asyncio
import logging
from typing import Dict, Any
from datetime import datetime

# Import new agents
from new_specialized_agents import (
    SocialMediaAgent, ECommerceAgent, CustomerServiceAgent,
    AnalyticsAgent, AutomationAgent
)

from new_super_agents import (
    DigitalMarketingSuperAgent, ECommerceSuperAgent,
    CustomerExperienceSuperAgent, BusinessIntelligenceSuperAgent,
    ProcessOptimizationSuperAgent
)

# Import existing system components
from agent_communication_hub import AgentCommunicationHub
from initialize_system import SystemInitializer

class NewAgentRegistrar:
    """Register and integrate new agents with the existing system"""
    
    def __init__(self):
        self.hub = None
        self.system_initializer = SystemInitializer()
        self.new_specialized_agents = {}
        self.new_super_agents = {}
        
    async def initialize_system(self):
        """Initialize the communication hub and system"""
        try:
            # Initialize the communication hub
            await self.system_initializer.initialize_communication_hub()
            self.hub = self.system_initializer.hub
            
            if not self.hub:
                raise Exception("Failed to initialize communication hub")
            
            logging.info("✅ Communication hub initialized for new agents")
            return True
            
        except Exception as e:
            logging.error(f"❌ Failed to initialize system: {e}")
            return False
    
    async def register_new_specialized_agents(self):
        """Register all new specialized agents"""
        try:
            # Create instances of new specialized agents
            new_agents = {
                'social_media_agent': SocialMediaAgent(),
                'ecommerce_agent': ECommerceAgent(),
                'customer_service_agent': CustomerServiceAgent(),
                'analytics_agent': AnalyticsAgent(),
                'automation_agent': AutomationAgent()
            }
            
            # Register each agent with the hub
            for agent_name, agent_instance in new_agents.items():
                # Create wrapper function for agent methods
                def create_agent_wrapper(agent, method_name):
                    async def wrapper(params={}):
                        try:
                            if hasattr(agent, method_name):
                                return await getattr(agent, method_name)(params)
                            else:
                                return {
                                    'status': 'error',
                                    'agent': agent.__class__.__name__,
                                    'error': f'Method {method_name} not found',
                                    'timestamp': datetime.now().isoformat()
                                }
                        except Exception as e:
                            return {
                                'status': 'error',
                                'agent': agent.__class__.__name__,
                                'error': str(e),
                                'timestamp': datetime.now().isoformat()
                            }
                    return wrapper
                
                # Register with appropriate method
                if agent_name == 'social_media_agent':
                    self.hub.register_agent(agent_name, create_agent_wrapper(agent_instance, 'create_content_calendar'))
                elif agent_name == 'ecommerce_agent':
                    self.hub.register_agent(agent_name, create_agent_wrapper(agent_instance, 'optimize_product_listings'))
                elif agent_name == 'customer_service_agent':
                    self.hub.register_agent(agent_name, create_agent_wrapper(agent_instance, 'handle_customer_inquiry'))
                elif agent_name == 'analytics_agent':
                    self.hub.register_agent(agent_name, create_agent_wrapper(agent_instance, 'analyze_business_metrics'))
                elif agent_name == 'automation_agent':
                    self.hub.register_agent(agent_name, create_agent_wrapper(agent_instance, 'create_automation_workflow'))
                
                self.new_specialized_agents[agent_name] = agent_instance
                logging.info(f"✅ Registered new specialized agent: {agent_name}")
            
            logging.info(f"✅ Successfully registered {len(new_agents)} new specialized agents")
            return True
            
        except Exception as e:
            logging.error(f"❌ Failed to register new specialized agents: {e}")
            return False
    
    async def register_new_super_agents(self):
        """Register all new super agents"""
        try:
            # Create instances of new super agents
            new_super_agents = {
                'digital_marketing_super_agent': DigitalMarketingSuperAgent(),
                'ecommerce_super_agent': ECommerceSuperAgent(),
                'customer_experience_super_agent': CustomerExperienceSuperAgent(),
                'business_intelligence_super_agent': BusinessIntelligenceSuperAgent(),
                'process_optimization_super_agent': ProcessOptimizationSuperAgent()
            }
            
            # Register each super agent with the hub
            for agent_name, agent_instance in new_super_agents.items():
                # Create wrapper function for super agent methods
                def create_super_agent_wrapper(agent, method_name):
                    async def wrapper(params={}):
                        try:
                            if hasattr(agent, method_name):
                                return await getattr(agent, method_name)(params)
                            else:
                                return {
                                    'status': 'error',
                                    'super_agent': agent.__class__.__name__,
                                    'error': f'Method {method_name} not found',
                                    'timestamp': datetime.now().isoformat()
                                }
                        except Exception as e:
                            return {
                                'status': 'error',
                                'super_agent': agent.__class__.__name__,
                                'error': str(e),
                                'timestamp': datetime.now().isoformat()
                            }
                    return wrapper
                
                # Register with appropriate orchestration method
                if agent_name == 'digital_marketing_super_agent':
                    self.hub.register_agent(agent_name, create_super_agent_wrapper(agent_instance, 'orchestrate_digital_marketing'))
                elif agent_name == 'ecommerce_super_agent':
                    self.hub.register_agent(agent_name, create_super_agent_wrapper(agent_instance, 'orchestrate_ecommerce_operations'))
                elif agent_name == 'customer_experience_super_agent':
                    self.hub.register_agent(agent_name, create_super_agent_wrapper(agent_instance, 'orchestrate_customer_experience'))
                elif agent_name == 'business_intelligence_super_agent':
                    self.hub.register_agent(agent_name, create_super_agent_wrapper(agent_instance, 'orchestrate_business_intelligence'))
                elif agent_name == 'process_optimization_super_agent':
                    self.hub.register_agent(agent_name, create_super_agent_wrapper(agent_instance, 'orchestrate_process_optimization'))
                
                self.new_super_agents[agent_name] = agent_instance
                logging.info(f"✅ Registered new super agent: {agent_name}")
            
            logging.info(f"✅ Successfully registered {len(new_super_agents)} new super agents")
            return True
            
        except Exception as e:
            logging.error(f"❌ Failed to register new super agents: {e}")
            return False
    
    async def test_new_agents(self):
        """Test all new agents to ensure they're working properly"""
        try:
            test_results = {
                'specialized_agents': {},
                'super_agents': {},
                'overall_status': 'success'
            }
            
            # Test specialized agents
            for agent_name, agent_instance in self.new_specialized_agents.items():
                try:
                    if agent_name == 'social_media_agent':
                        result = await agent_instance.create_content_calendar({
                            'platform': 'all',
                            'duration': 7,
                            'theme': 'test'
                        })
                    elif agent_name == 'ecommerce_agent':
                        result = await agent_instance.optimize_product_listings({
                            'products': [{'title': 'Test Product', 'description': 'Test Description'}],
                            'platform': 'shopify'
                        })
                    elif agent_name == 'customer_service_agent':
                        result = await agent_instance.handle_customer_inquiry({
                            'inquiry': 'Test inquiry',
                            'customer_info': {},
                            'channel': 'email'
                        })
                    elif agent_name == 'analytics_agent':
                        result = await agent_instance.analyze_business_metrics({
                            'data': {'test_metric': 100},
                            'metrics': ['test_metric'],
                            'timeframe': '7_days'
                        })
                    elif agent_name == 'automation_agent':
                        result = await agent_instance.create_automation_workflow({
                            'workflow_type': 'test',
                            'triggers': ['time_based'],
                            'actions': ['email']
                        })
                    
                    test_results['specialized_agents'][agent_name] = {
                        'status': 'success',
                        'result': result.get('status', 'unknown')
                    }
                    
                except Exception as e:
                    test_results['specialized_agents'][agent_name] = {
                        'status': 'error',
                        'error': str(e)
                    }
                    test_results['overall_status'] = 'partial_success'
            
            # Test super agents
            for agent_name, agent_instance in self.new_super_agents.items():
                try:
                    if agent_name == 'digital_marketing_super_agent':
                        result = await agent_instance.orchestrate_digital_marketing({
                            'campaign_type': 'test',
                            'budget': 100,
                            'duration': 7,
                            'platforms': ['facebook']
                        })
                    elif agent_name == 'ecommerce_super_agent':
                        result = await agent_instance.orchestrate_ecommerce_operations({
                            'operation_type': 'test',
                            'products': [],
                            'platform': 'shopify'
                        })
                    elif agent_name == 'customer_experience_super_agent':
                        result = await agent_instance.orchestrate_customer_experience({
                            'customer_data': {},
                            'support_channels': ['email'],
                            'experience_goals': {}
                        })
                    elif agent_name == 'business_intelligence_super_agent':
                        result = await agent_instance.orchestrate_business_intelligence({
                            'data_sources': ['test'],
                            'analysis_type': 'test',
                            'business_goals': {}
                        })
                    elif agent_name == 'process_optimization_super_agent':
                        result = await agent_instance.orchestrate_process_optimization({
                            'processes': [],
                            'optimization_goals': {},
                            'automation_level': 'low'
                        })
                    
                    test_results['super_agents'][agent_name] = {
                        'status': 'success',
                        'result': result.get('status', 'unknown')
                    }
                    
                except Exception as e:
                    test_results['super_agents'][agent_name] = {
                        'status': 'error',
                        'error': str(e)
                    }
                    test_results['overall_status'] = 'partial_success'
            
            logging.info(f"✅ Agent testing completed with status: {test_results['overall_status']}")
            return test_results
            
        except Exception as e:
            logging.error(f"❌ Failed to test new agents: {e}")
            return {
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }
    
    async def get_system_status(self):
        """Get comprehensive system status including new agents"""
        try:
            if not self.hub:
                return {
                    'status': 'error',
                    'message': 'System not initialized',
                    'timestamp': datetime.now().isoformat()
                }
            
            # Get hub status
            hub_status = self.hub.get_status_report()
            
            # Count new agents
            new_agent_count = len(self.new_specialized_agents) + len(self.new_super_agents)
            
            return {
                'status': 'success',
                'system_status': {
                    'total_agents': hub_status.get('total_agents', 0),
                    'new_specialized_agents': len(self.new_specialized_agents),
                    'new_super_agents': len(self.new_super_agents),
                    'new_agent_total': new_agent_count,
                    'hub_operational': True
                },
                'new_agents': {
                    'specialized': list(self.new_specialized_agents.keys()),
                    'super_agents': list(self.new_super_agents.keys())
                },
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            return {
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }

async def main():
    """Main function to register and test new agents"""
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    
    logger.info("🚀 Starting new agent registration process...")
    
    # Create registrar
    registrar = NewAgentRegistrar()
    
    # Initialize system
    if not await registrar.initialize_system():
        logger.error("❌ Failed to initialize system")
        return
    
    # Register new specialized agents
    if not await registrar.register_new_specialized_agents():
        logger.error("❌ Failed to register new specialized agents")
        return
    
    # Register new super agents
    if not await registrar.register_new_super_agents():
        logger.error("❌ Failed to register new super agents")
        return
    
    # Test all new agents
    test_results = await registrar.test_new_agents()
    logger.info(f"🧪 Agent testing results: {test_results['overall_status']}")
    
    # Get final system status
    system_status = await registrar.get_system_status()
    logger.info(f"📊 System status: {system_status}")
    
    logger.info("🎉 New agent registration process completed successfully!")

if __name__ == "__main__":
    asyncio.run(main())
