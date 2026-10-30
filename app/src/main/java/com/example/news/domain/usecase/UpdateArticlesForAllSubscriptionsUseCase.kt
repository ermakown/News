package com.example.news.domain.usecase

import com.example.news.domain.repository.NewsRepository
import kotlinx.coroutines.flow.Flow
import javax.inject.Inject

class UpdateArticlesForAllSubscriptionsUseCase @Inject constructor(
    private val repository: NewsRepository
) {

    suspend operator fun invoke() {
        repository.updateArticlesForAllSubscriptions()
    }
}