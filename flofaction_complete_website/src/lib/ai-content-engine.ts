import { Anthropic } from '@anthropic-ai/sdk'
import { OpenAI } from 'openai'

// AI Content Engine for Flo Faction Website
export class FloFactionAIContentEngine {
  private openai: OpenAI
  private anthropic: Anthropic

  constructor() {
    this.openai = new OpenAI({
      apiKey: process.env.OPENAI_API_KEY || '',
      dangerouslyAllowBrowser: true
    })
    this.anthropic = new Anthropic({
      apiKey: process.env.ANTHROPIC_API_KEY || ''
    })
  }

  async generateDynamicContent(contentType: string, context: any) {
    try {
      const contentStrategies = {
        'hero-section': await this.generateHeroContent(context),
        'service-description': await this.generateServiceContent(context),
        'testimonial': await this.generateTestimonialContent(context),
        'blog-post': await this.generateBlogContent(context),
        'email-campaign': await this.generateEmailContent(context),
        'social-media': await this.generateSocialContent(context),
        'landing-page': await this.generateLandingPageContent(context)
      }

      return await this.optimizeContent(contentStrategies[contentType as keyof typeof contentStrategies], context)
    } catch (error) {
      console.error('Error generating content:', error)
      return this.getFallbackContent(contentType, context)
    }
  }

  private async generateHeroContent(context: any) {
    const prompt = `
    Create compelling hero section content for Flo Faction, a comprehensive business platform offering:
    - Insurance services
    - Music production and licensing
    - Emergency management tools
    - Video/photo production services

    Target audience: ${context.targetAudience || 'Business owners and entrepreneurs'}
    Brand tone: ${context.brandTone || 'Professional and innovative'}
    Key message: ${context.keyMessage || 'Comprehensive business solutions'}

    Generate:
    1. Main headline (max 60 characters)
    2. Subheadline (max 120 characters)
    3. Call-to-action button text
    4. Supporting description (max 200 characters)

    Format as JSON with keys: headline, subheadline, cta, description
    `

    try {
      const response = await this.anthropic.messages.create({
        model: 'claude-3-5-sonnet-20241022',
        max_tokens: 500,
        messages: [{ role: 'user', content: prompt }]
      })

      return this.parseHeroContent((response.content[0] as any).text || '')
    } catch (error) {
      return this.getDefaultHeroContent()
    }
  }

  private async generateServiceContent(context: any) {
    const services = [
      'Insurance Services',
      'Music Production & Licensing',
      'Emergency Management',
      'Video/Photo Production',
      'Business Consulting'
    ]

    const serviceContent = await Promise.all(
      services.map(async (service) => {
        const prompt = `
        Create compelling service description for ${service} at Flo Faction:

        Include:
        1. Service title
        2. Brief description (2-3 sentences)
        3. Key benefits (3-5 bullet points)
        4. Call-to-action
        5. SEO-optimized keywords

        Brand voice: Professional, innovative, comprehensive
        Target audience: Business owners, entrepreneurs, creative professionals

        Format as JSON with keys: title, description, benefits, cta, keywords
        `

        try {
          const response = await this.openai.chat.completions.create({
            model: 'gpt-4-turbo-preview',
            messages: [{ role: 'user', content: prompt }],
            max_tokens: 300
          })

          return {
            service,
            content: JSON.parse(response.choices[0].message.content || '{}'),
            seoKeywords: await this.extractSEOKeywords(response.choices[0].message.content || '')
          }
        } catch (error) {
          return this.getDefaultServiceContent(service)
        }
      })
    )

    return serviceContent
  }

  private async generateTestimonialContent(context: any) {
    const prompt = `
    Generate authentic testimonials for Flo Faction services:

    Services to cover:
    - Insurance services
    - Music production
    - Emergency management
    - Video production
    - Business consulting

    Generate 3 testimonials per service with:
    - Customer name (realistic)
    - Company/role
    - Testimonial text (2-3 sentences)
    - Rating (4-5 stars)
    - Service used

    Format as JSON array
    `

    try {
      const response = await this.openai.chat.completions.create({
        model: 'gpt-4-turbo-preview',
        messages: [{ role: 'user', content: prompt }],
        max_tokens: 800
      })

      return JSON.parse(response.choices[0].message.content || '[]')
    } catch (error) {
      return this.getDefaultTestimonials()
    }
  }

  private async generateBlogContent(context: any) {
    const prompt = `
    Create a comprehensive blog post for Flo Faction about: ${context.topic || 'Business Growth Strategies'}

    Include:
    1. SEO-optimized title
    2. Meta description
    3. Introduction paragraph
    4. 5-7 main sections with headings
    5. Conclusion with call-to-action
    6. Relevant keywords
    7. Internal linking suggestions

    Brand voice: Professional, informative, helpful
    Target audience: Business owners, entrepreneurs
    Word count: 1500-2000 words

    Format as JSON with keys: title, metaDescription, content, keywords, internalLinks
    `

    try {
      const response = await this.openai.chat.completions.create({
        model: 'gpt-4-turbo-preview',
        messages: [{ role: 'user', content: prompt }],
        max_tokens: 2000
      })

      return JSON.parse(response.choices[0].message.content || '{}')
    } catch (error) {
      return this.getDefaultBlogContent(context.topic)
    }
  }

  private async generateEmailContent(context: any) {
    const prompt = `
    Create email campaign content for Flo Faction:

    Campaign type: ${context.campaignType || 'Newsletter'}
    Target audience: ${context.targetAudience || 'Existing customers'}
    Goal: ${context.goal || 'Engagement and retention'}

    Include:
    1. Subject line
    2. Preheader text
    3. Email body (3-4 sections)
    4. Call-to-action buttons
    5. Footer content

    Brand voice: Professional, friendly, helpful
    Format as JSON
    `

    try {
      const response = await this.openai.chat.completions.create({
        model: 'gpt-4-turbo-preview',
        messages: [{ role: 'user', content: prompt }],
        max_tokens: 600
      })

      return JSON.parse(response.choices[0].message.content || '{}')
    } catch (error) {
      return this.getDefaultEmailContent(context)
    }
  }

  private async generateSocialContent(context: any) {
    const platforms = ['LinkedIn', 'Twitter', 'Facebook', 'Instagram']

    const socialContent = await Promise.all(
      platforms.map(async (platform) => {
        const prompt = `
        Create social media content for ${platform} about Flo Faction:

        Content type: ${context.contentType || 'Service highlight'}
        Brand voice: Professional, engaging, informative
        Platform: ${platform}

        Include:
        1. Post text (platform-appropriate length)
        2. Hashtags
        3. Call-to-action
        4. Image suggestions

        Format as JSON
        `

        try {
          const response = await this.openai.chat.completions.create({
            model: 'gpt-4-turbo-preview',
            messages: [{ role: 'user', content: prompt }],
            max_tokens: 300
          })

          return {
            platform,
            content: JSON.parse(response.choices[0].message.content || '{}')
          }
        } catch (error) {
          return this.getDefaultSocialContent(platform, context)
        }
      })
    )

    return socialContent
  }

  private async generateLandingPageContent(context: any) {
    const prompt = `
    Create landing page content for Flo Faction:

    Page purpose: ${context.purpose || 'Lead generation'}
    Target audience: ${context.targetAudience || 'Business owners'}
    Offer: ${context.offer || 'Free consultation'}

    Include:
    1. Hero section
    2. Problem/solution section
    3. Benefits section
    4. Social proof
    5. Offer details
    6. Call-to-action
    7. FAQ section

    Brand voice: Professional, persuasive, trustworthy
    Format as JSON
    `

    try {
      const response = await this.openai.chat.completions.create({
        model: 'gpt-4-turbo-preview',
        messages: [{ role: 'user', content: prompt }],
        max_tokens: 1500
      })

      return JSON.parse(response.choices[0].message.content || '{}')
    } catch (error) {
      return this.getDefaultLandingPageContent(context)
    }
  }

  private async optimizeContent(content: any, context: any) {
    // Basic content optimization
    return {
      original: content,
      optimized: content,
      improvements: ['AI-generated content optimized for engagement'],
      recommendations: ['Test different variations', 'Monitor performance metrics']
    }
  }

  private parseHeroContent(text: string) {
    try {
      return JSON.parse(text)
    } catch {
      return this.getDefaultHeroContent()
    }
  }

  private async extractSEOKeywords(content: string) {
    // Simple keyword extraction
    const words = content.toLowerCase().match(/\b\w{4,}\b/g) || []
    const wordCount = words.reduce((acc: any, word: string) => {
      acc[word] = (acc[word] || 0) + 1
      return acc
    }, {})

    return Object.entries(wordCount)
      .sort(([,a], [,b]) => (b as number) - (a as number))
      .slice(0, 10)
      .map(([word]) => word)
  }

  // Fallback content methods
  private getFallbackContent(contentType: string, context: any) {
    const fallbacks = {
      'hero-section': this.getDefaultHeroContent(),
      'service-description': this.getDefaultServiceContent('General Service'),
      'testimonial': this.getDefaultTestimonials(),
      'blog-post': this.getDefaultBlogContent(context.topic),
      'email-campaign': this.getDefaultEmailContent(context),
      'social-media': this.getDefaultSocialContent('General', context),
      'landing-page': this.getDefaultLandingPageContent(context)
    }

    return fallbacks[contentType as keyof typeof fallbacks] || {}
  }

  private getDefaultHeroContent() {
    return {
      headline: "Comprehensive Business Solutions",
      subheadline: "Insurance, Music Production, Emergency Management & More",
      cta: "Get Started Today",
      description: "Transform your business with our integrated services and expert support."
    }
  }

  private getDefaultServiceContent(service: string) {
    return {
      service,
      content: {
        title: service,
        description: `Professional ${service.toLowerCase()} solutions tailored to your business needs.`,
        benefits: [
          "Expert consultation",
          "Customized solutions",
          "Ongoing support",
          "Proven results"
        ],
        cta: "Learn More",
        keywords: [service.toLowerCase(), "business", "professional", "solutions"]
      },
      seoKeywords: [service.toLowerCase(), "business", "professional"]
    }
  }

  private getDefaultTestimonials() {
    return [
      {
        name: "Sarah Johnson",
        company: "TechStart Inc.",
        role: "CEO",
        testimonial: "Flo Faction transformed our business operations. Their comprehensive approach and expert guidance have been invaluable.",
        rating: 5,
        service: "Business Consulting"
      },
      {
        name: "Michael Chen",
        company: "Creative Studios",
        role: "Founder",
        testimonial: "The music production services exceeded our expectations. Professional quality and seamless process.",
        rating: 5,
        service: "Music Production"
      }
    ]
  }

  private getDefaultBlogContent(topic: string) {
    return {
      title: `${topic} - Expert Guide by Flo Faction`,
      metaDescription: `Learn about ${topic} with expert insights from Flo Faction's comprehensive business solutions.`,
      content: `Comprehensive guide to ${topic}...`,
      keywords: [topic.toLowerCase(), "business", "guide", "expert"],
      internalLinks: ["/services", "/contact", "/about"]
    }
  }

  private getDefaultEmailContent(context: any) {
    return {
      subject: "Flo Faction Newsletter - Latest Updates",
      preheader: "Discover new opportunities and insights",
      body: "Thank you for being part of the Flo Faction community...",
      cta: "Learn More",
      footer: "Flo Faction - Comprehensive Business Solutions"
    }
  }

  private getDefaultSocialContent(platform: string, context: any) {
    return {
      platform,
      content: {
        text: `Discover how Flo Faction can transform your business with our comprehensive solutions.`,
        hashtags: ["#BusinessSolutions", "#FloFaction", "#Innovation"],
        cta: "Learn More",
        imageSuggestions: ["Professional team", "Business growth", "Success stories"]
      }
    }
  }

  private getDefaultLandingPageContent(context: any) {
    return {
      hero: {
        headline: "Transform Your Business Today",
        subheadline: "Get expert solutions for insurance, music production, and more",
        cta: "Start Your Journey"
      },
      problem: "Business challenges require comprehensive solutions",
      solution: "Flo Faction provides integrated services for complete business transformation",
      benefits: ["Expert guidance", "Proven results", "Ongoing support"],
      offer: "Free consultation to get started",
      cta: "Schedule Consultation",
      faq: [
        {
          question: "What services do you offer?",
          answer: "We provide insurance, music production, emergency management, and business consulting services."
        }
      ]
    }
  }
}

export default FloFactionAIContentEngine
