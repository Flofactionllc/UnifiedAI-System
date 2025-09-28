// UnifiedAI Client for connecting to the backend agent system

const UNIFIEDAI_BASE_URL = process.env.UNIFIEDAI_BASE_URL || 'http://localhost:8000';

export class UnifiedAIClient {
  private baseUrl: string;

  constructor(baseUrl: string = UNIFIEDAI_BASE_URL) {
    this.baseUrl = baseUrl;
  }

  async requestAgent(agentName: string, params: any) {
    try {
      const response = await fetch(`${this.baseUrl}/api/agents/${agentName}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(params),
      });

      if (!response.ok) {
        throw new Error(`Agent ${agentName} request failed: ${response.statusText}`);
      }

      return await response.json();
    } catch (error) {
      console.error(`Error requesting agent ${agentName}:`, error);
      throw error;
    }
  }

  // Insurance Agent
  async generateInsuranceQuote(params: {
    insurance_type: string;
    age: number;
    health_status: string;
    coverage_amount: number;
  }) {
    return this.requestAgent('insurance_agent_automated', params);
  }

  // Music Supervisor Agent
  async analyzeMusic(params: {
    music_file: string;
    target_media: string;
    budget_range: string;
  }) {
    return this.requestAgent('music_supervisor_automated', params);
  }

  // Marketing Strategist Agent
  async createMarketingStrategy(params: {
    business_type: string;
    target_audience: string;
    budget: number;
    goals: string;
  }) {
    return this.requestAgent('marketing_strategist_automated', params);
  }

  // Business Consultant Agent
  async provideBusinessConsultation(params: {
    business_stage: string;
    industry: string;
    challenges: string;
    goals: string;
  }) {
    return this.requestAgent('business_consultant_automated', params);
  }

  // Video Producer Agent
  async generateVideoQuote(params: {
    project_type: string;
    duration: string;
    complexity: string;
    deadline: string;
  }) {
    return this.requestAgent('video_producer', params);
  }

  // Get all agents status
  async getAgentsStatus() {
    try {
      const response = await fetch(`${this.baseUrl}/api/agents/status`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (!response.ok) {
        throw new Error('Failed to fetch agents status');
      }

      return await response.json();
    } catch (error) {
      console.error('Error fetching agents status:', error);
      throw error;
    }
  }

  // Send message between agents
  async sendAgentMessage(fromAgent: string, toAgent: string, message: string, data?: any) {
    try {
      const response = await fetch(`${this.baseUrl}/api/agents/message`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          fromAgent,
          toAgent,
          message,
          data,
        }),
      });

      if (!response.ok) {
        throw new Error('Failed to send agent message');
      }

      return await response.json();
    } catch (error) {
      console.error('Error sending agent message:', error);
      throw error;
    }
  }
}

export const unifiedAIClient = new UnifiedAIClient();
